from flask import Flask, request, jsonify
from models.text_moderator import TextModerator
from models.image_moderator import ImageModerator
from models.video_moderator import VideoModerator

app = Flask(__name__)

text_moderator = TextModerator()
image_moderator = ImageModerator()
video_moderator = VideoModerator()

@app.route("/moderate/text", methods=["POST"])
def moderate_text():
    data = request.json
    content = data.get("content")
    if not content:
        return jsonify({"error": "No content provided."}), 400
    moderated_content = text_moderator.moderate_text(content)
    return jsonify({"moderated_content": moderated_content})

@app.route("/moderate/image", methods=["POST"])
def moderate_image():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided."}), 400
    file_path = f"uploads/{file.filename}"
    file.save(file_path)
    result = image_moderator.moderate_image(file_path)
    return jsonify({"result": result})

@app.route("/moderate/video", methods=["POST"])
def moderate_video():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided."}), 400
    file_path = f"uploads/{file.filename}"
    file.save(file_path)
    result = video_moderator.moderate_video(file_path)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
