from flask import Flask, request, render_template

import constants as con
import util
import descriptors


app = Flask(__name__)

detector = None
matcher = None
host_descriptors = None

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files["img"]

        if f.filename == '':
            render_template('index.html', fqdn="")

        img = util.read_img_from_bytes_grayscale(f.read())

        fqdn = get_img_host(detector, matcher, img)

        return render_template('index.html', fqdn=fqdn)

    return render_template('index.html', fqdn="")

def get_img_host(detector, matcher, img):
    img_desctiptors = descriptors.get_image_descriptors(detector, img)

    host, distance = descriptors.get_best_match(matcher, img_desctiptors, host_descriptors)

    if distance >= con.DISTANCE_THRESHOLD:
        return con.UNKNOWN_HOST

    return host

if __name__ == '__main__':
    detector = descriptors.get_detector(con.DETECTOR)
    matcher = descriptors.get_matcher(con.MATCHER)

    hosts = util.read_non_empty_lines(con.HOSTS_PATH)
    host_descriptors = descriptors.get_host_descriptors(detector, hosts)

    app.run(host="0.0.0.0")
