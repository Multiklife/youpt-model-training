from google.cloud import aiplatform

# Инициализация Vertex AI
aiplatform.init(project='dd17dd', location='us-central1')

def train_model():
    print("Начинаем обучение модели...")
    # Здесь идет процесс обучения модели

# Создаем задание на обучение
job = aiplatform.CustomJob.from_local_script(
    display_name="youpt_model_training",
    script_path="train_model.py",
    container_uri="gcr.io/dd17dd/custom-training-container:latest",
    requirements=["google-cloud-aiplatform"],
)

job.run()
