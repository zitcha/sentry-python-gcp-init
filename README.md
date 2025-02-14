# sentry-python-gcp-init

Adds the Sentry's Python SDK. To send events such as errors or traces from your Google Compute into Sentry.

# How to use

Add into your `requirements.txt`:
```
git+https://github.com/zitcha/sentry-python-gcp-init.git#egg=zitcha_sentry_python_gcp_init
```

## Required Environment Variables
| Variable             | Description |
|----------------------|-------------|
| `SENTRY_DSN_URL`     | This is your project's Sentry client key; this value can be retrieved in your Sentry project. |
| `PROJECT_ID`         | The Google project ID where the compute resources would use this package. This is used for [Sentry environment](https://docs.sentry.io/concepts/key-terms/environments/). |
| `SENTRY_SAMPLE_RATE` | The [traces sample rate](https://docs.sentry.io/platforms/javascript/configuration/sampling/#setting-a-uniform-sample-rate) as a decimal value, e.g., 0.5 = 50%; 1 = 100%. Default is 1.0. |

## Import the module
```python
import zitcha_sentry_python_gcp_init
...
```
