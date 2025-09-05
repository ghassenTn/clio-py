import json
import os
from datetime import datetime

class Cache:
    """A simple file-based cache for storing facts."""
    def __init__(self, cache_dir='.cache'):
        self.cache_dir = cache_dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        self.cache_file = os.path.join(self.cache_dir, 'facts.json')
        self.cache = self._load_cache()

    def _load_cache(self):
        """Loads the cache from a file."""
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        """Saves the cache to a file."""
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=4)

    def get(self, key):
        """Gets a value from the cache."""
        return self.cache.get(key)

    def set(self, key, value, source=None, certainty=None):
        """Sets a value in the cache with metadata."""
        self.cache[key] = {
            'value': value,
            'timestamp': datetime.now().isoformat(),
            'source': source,
            'certainty': certainty
        }
        self._save_cache()