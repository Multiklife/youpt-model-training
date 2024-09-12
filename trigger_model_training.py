from google.cloud import aiplatform

def trigger_model_training(event, context):
    aiplatform.init(project='dd17dd', location='us-central1')

    job = aiplatform.CustomJob.from_local_script(
        display_name="youpt_model_training",
        script_path="train_model.py",
        container_uri="gcr.io/dd17dd/custom-training-container:latest",
        requirements=["google-cloud-aiplatform"],
    )

    job.run()
