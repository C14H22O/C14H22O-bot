def get_links_json(button_id: int, name: str, url: str) -> dict:
    return {
        "id": str(button_id),
        "render_data": {
            "label": name,
            "visited_label": name
        },
        "action": {
            "type": 0,
            "permission": {
                "type": 2
            },
            "data": url
        }
    }
