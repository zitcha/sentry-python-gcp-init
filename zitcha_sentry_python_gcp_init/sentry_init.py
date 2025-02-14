import os
import sentry_sdk

from sentry_sdk.integrations.gcp import GcpIntegration

def init_sentry():
    dsn_url = os.environ.get("SENTRY_DSN_URL", "")
    project_id = os.environ.get("PROJECT_ID", "")
    sample_rate = float(os.environ.get("SENTRY_SAMPLE_RATE", "1.0"))
    
    sentry_sdk.init(
        dsn=dsn_url,
        integrations=[GcpIntegration()],
        traces_sample_rate=sample_rate,
        environment=project_id
    )
