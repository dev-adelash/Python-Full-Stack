from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'shared-python'))
from api import create_app
app=create_app(Path(__file__).resolve().parent.parent/'project.json')
