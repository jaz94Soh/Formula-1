import json

class Track:
    def __init__(self, track_name, corner, overtake):
        self.track_name = track_name
        self.corner = corner
        self.overtake = overtake
        self.brakingpoint = None
        self.entryspeed = None
        self.cornerspeed = None

    def update(self, new_data):
        if 'brakingpoint' in new_data:
            self.brakingpoint = new_data['brakingpoint']
        if 'entryspeed' in new_data:
            self.entryspeed = new_data['entryspeed']
        if 'cornerspeed' in new_data:
            self.cornerspeed = new_data['cornerspeed']

    def to_dict(self):
        return {
            "Name": self.track_name,
            "corner": self.corner,
            "overtake": self.overtake,
            "brakingpoint": self.brakingpoint,
            "entryspeed": self.entryspeed,
            "cornerspeed": self.cornerspeed
        }

class TrackManager:
    def __init__(self, json_file):
        self.Tracks = []
        self.json_file = json_file
        self.load_Track_from_json()

    def load_Track_from_json(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
            for track_data in data['Tracks']:
                track = Track(track_data['track_name'], track_data['corner'], track_data['overtake'])
                track.brakingpoint = track_data.get('brakingpoint')
                track.entryspeed = track_data.get('entryspeed')
                track.cornerspeed = track_data.get('cornerspeed')
                self.Tracks.append(track)

    def update_car_data(self, track_name, new_data):
        for track in self.Tracks:
            if track.track_name == track_name:
                track.update(new_data)
                break

    def save_cars_to_json(self):
        tracks_list = [track.to_dict() for track in self.Tracks]
        with open(self.json_file, 'w') as file:
            json.dump({"tracks": tracks_list}, file, indent=4)
  