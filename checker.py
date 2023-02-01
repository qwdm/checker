import yaml
import requests
import datetime
from prometheus_client import Gauge, push_to_gateway, CollectorRegistry

AUXILIARY_KEYS = ['params', 'data', 'json', 'headers'] 


def prometheus(pushgateway_url: str, results: list[dict]):
    registry = CollectorRegistry()
    for result in results:
        g = Gauge(f"checker_{result['app']}", "Health check of a given app", registry=registry)
        g.set(int(result['is_working']))
        push_to_gateway(pushgateway_url, job='checker', registry=registry)


def main(conf: dict):
    apps = conf['apps_to_check']

    results = []
    for app_name, app_conf in apps.items():
        kwargs = {key: app_conf[key] for key in AUXILIARY_KEYS if app_conf.get(key) is not None}
        kwargs['timeout'] = app_conf.get('timeout') or conf['default_timeout']
        try:
            r = requests.request(app_conf['method'], app_conf['url'], **kwargs)
        except requests.exceptions.Timeout:
            is_working = False
            reason = 'timeout'
        except Exception as e:
            is_working = False
            reason = str(e)[:200]
        else:
            is_working = (r.status_code == app_conf['expected_status_code'])
            reason = r.status_code

        result = {
            'app': app_name,
            'is_working': is_working,
            'reason': reason,
            'datetime': datetime.datetime.utcnow().isoformat(),
        }
        results.append(result)

        print(result)  # TODO send to graphana

    prometheus(conf['pushgateway'], results)


if __name__ == "__main__":
    with open('config.yml') as f:
        conf = yaml.load(f, yaml.Loader)

    main(conf)
    



