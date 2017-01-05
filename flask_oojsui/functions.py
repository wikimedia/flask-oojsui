import os

from flask import Blueprint, send_from_directory

DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def build_static_blueprint(*args, **kwargs):
    bp = Blueprint(*args, **kwargs)

    @bp.route('/oojs-ui-static/<path:fn>')
    def oojsui_static(fn):
        return send_from_directory(
            os.path.join(DIRECTORY, "static", "oojs-ui"), fn)

    @bp.route('/oojs-ui-static/dist/<path:fn>')
    def oojsui_static_dist(fn):
        return send_from_directory(
            os.path.join(DIRECTORY, "static", "oojs-ui"), fn)

    @bp.route('/oojs-static/<path:fn>')
    def oojs_static(fn):
        return send_from_directory(
            os.path.join(DIRECTORY, "static", "oojs"), fn)

    @bp.route('/oojs-static/dist/<path:fn>')
    def oojs_static_dist(fn):
        return send_from_directory(
            os.path.join(DIRECTORY, "static", "oojs"), fn)

    return bp
