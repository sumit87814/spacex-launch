from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def latest_launch():
    url = "https://api.spacexdata.com/v4/launches/latest"
    launch_data = requests.get(url).json()

    # Extract required data
    launch_name = launch_data.get("name", "N/A")
    launch_date = launch_data.get("date_utc", "N/A")
    rocket_id = launch_data.get("rocket", "N/A")
    launchpad_id = launch_data.get("launchpad", "N/A")

    # Fetch rocket name
    rocket_name = requests.get(f"https://api.spacexdata.com/v4/rockets/{rocket_id}").json().get("name", "N/A")

    # Fetch launchpad name
    launchpad_name = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}").json().get("name", "N/A")

    return render_template("launch.html",
                           launch_name=launch_name,
                           launch_date=launch_date,
                           rocket_name=rocket_name,
                           launchpad_name=launchpad_name)

@app.route('/past_count')
def past_launch_count():
    url = "https://api.spacexdata.com/v4/launches"
    past_launches = requests.get(url).json()
    count = len(past_launches)
    return render_template("past_count.html", count=count)

if __name__ == "__main__":
    app.run(debug=True)
