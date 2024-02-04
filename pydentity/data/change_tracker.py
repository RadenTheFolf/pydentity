class ChangeTracker:
    def __init__(self, data: dict):
        self.data = data
        self.old_data = data
        self.changes = []

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        if not key in self.old_data:
            self.old_data[key] = value
        self.changes.append((key, value))

    def __delitem__(self, key):
        del self.data[key]
        self.changes.append((key, None))

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)

    def get_changes(self):
        return self.changes

    def clear_changes(self):
        self.changes = []

    def get_data(self):
        return self.data

    def set_data(self, data: dict):
        self.data = data
        self.old_data = data
        self.clear_changes()

    def get_original_data(self):
        return self.old_data

