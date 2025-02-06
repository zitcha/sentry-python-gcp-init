import os
import urllib.request
import sentry_sdk

from sentry_sdk.integrations.gcp import GcpIntegration

def init_sentry():
    dsn_url = os.environ.get("SENTRY_DSN_URL")
    if not dsn_url:
        raise ValueError("The SENTRY_DSN_URL environment variable is not set.")

    project_id = os.environ.get("PROJECT_ID")
    if not project_id:
        raise ValueError("The PROJECT_ID environment variable is not set.")
    
    sentry_sdk.init(
        dsn=dsn_url,
        integrations=[GcpIntegration()],
        traces_sample_rate=1.0,
        environment=project_id
    )
