# NAYANTRA-360° - Model Downloader - Run First
import os
os.makedirs("models", exist_ok=True)
os.makedirs("static/images", exist_ok=True)

print("=== NAYANTRA-360° Model Downloader ===")
try:
    from ultralytics import YOLO
    print("Downloading YOLOv8n for PPE, Mobile, Person, Objects...")
    YOLO("yolov8n.pt")
    print("✓ YOLOv8n ready")
except Exception as e:
    print(f"YOLO will auto-download: {e}")

try:
    import whisper
    print("Downloading Whisper base for whisper analysis...")
    whisper.load_model("base")
    print("✓ Whisper base ready")
except Exception as e:
    print(f"Whisper will auto-download: {e}")

print("✓ Mediapipe models auto-download on first use")
print("✓ Coqui TTS XTTS-v2 for voice clone downloads on first use")
print("=== All Models Ready for NAYANTRA-360° ===")
print("Put the 3 generated images into static/images/ as:")
print("- hero.jpg, architecture.jpg, problem.jpg")
