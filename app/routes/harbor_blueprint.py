from app.controllers.harbor_controller import (
    get_one_harbor,
    create_harbor,
    update_one_harbor,
    delete_one_harbor,
    get_containers_on_harbor_all_times,
    get_containers_on_harbor_now,
    update_containers_on_harbor,
    get_ships_on_harbor_now,
    get_ships_on_harbor_all_times,
    update_ships_on_harbor
)
from flask import Blueprint

bp = Blueprint('harbor_bp', __name__, url_prefix='/harbor')

harbor_name: str
containers_on_harbor_now: str
containers_on_harbor_all_times: str
update_one_container_on_harbor: str
ships_on_harbor_now: str
ships_on_harbor_all_times: str
update_one_ship_on_harbor: str

bp.post('')(create_harbor)
bp.post("/update_one_container_on_harbor")(update_containers_on_harbor)
bp.post("/update_one_ship_on_harbor")(update_ships_on_harbor)
bp.get("/harbor_name")(get_one_harbor)
bp.get("/containers_on_harbor_now")(get_containers_on_harbor_now)
bp.get("/containers_on_harbor_all_times")(get_containers_on_harbor_all_times)
bp.get("/ships_on_harbor_now")(get_ships_on_harbor_now)
bp.get("/ships_on_harbor_all_times")(get_ships_on_harbor_all_times)
bp.patch("/harbor_name")(update_one_harbor)
bp.delete("/harbor_name")(delete_one_harbor)
