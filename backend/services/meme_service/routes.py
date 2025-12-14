from flask import Blueprint, request, jsonify
from .repository import create_meme

bp = Blueprint("memes", __name__)

@bp.route("/memes", methods=["POST"])
def post_meme():
    data = request.json
    meme = create_meme(
        user_id=data["user_id"],
        image_url=data["image_url"],
        caption=data.get("caption", "")
    )
    return jsonify(meme), 201