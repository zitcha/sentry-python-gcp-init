# sentry-python-gcp-init

Adds the Sentry's Python SDK. To send events such as errors or traces from your Google Compute into Sentry.

# How to use

Add into your `requirements.txt`:
```
git+https://github.com/zitcha/sentry-python-gcp-init.git#egg=zitcha_sentry_init
```

## Required Environment Variables
| Variable           | Description |
|--------------------|-------------|
| `SENTRY_DSN_URL`   | This is your project's Sentry client key; this value can be retrieved in your Sentry project. |
| `PROJECT_ID`       | The Google project ID where the compute resources would use this package. This is used for [Sentry environment](https://docs.sentry.io/concepts/key-terms/environments/). |

## Import the module
```python
import zitcha_sentry_python_gcp_init
...
```
