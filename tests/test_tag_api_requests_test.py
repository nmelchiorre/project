import os
from random import randint

import requests
from simple_settings import settings


class TestTagAPIRequests:
    os.environ["SIMPLE_SETTINGS"] = "settings.base"

    def test_tag_api_requests(self):
        tag_name = f"Test_tag {randint(1, 100)}"
        # test PUT request to create a tag for vulnerability.
        put = requests.put(
            "https://ce.contrastsecurity.com/Contrast/api/ng/b72cd362-9374-40a1-a9b2-f4720b522874/tags/traces",
            headers={
                'Authorization': f'{settings.Contrast.AdminUser().auth}',
                'API-Key': f'{settings.Contrast.AdminUser().api_key}',
                'Content-Type': 'application/json'
            },
            json={"tags": [f"{tag_name}"], "traces_id": ["2ASW-K5P0-LPPB-PQ36"]}
            )
        assert put.status_code == 200

        # test GET request to verify new tag was created for vulnerability.
        get = requests.get(
            "https://ce.contrastsecurity.com/Contrast/api/ng/b72cd362-9374-40a1-a9b2-f4720b522874/tags/traces/trace/2ASW-K5P0-LPPB-PQ36",
            headers={
                'Authorization': f'{settings.Contrast.AdminUser().auth}',
                'API-Key': f'{settings.Contrast.AdminUser().api_key}',
                'Content-Type': 'application/json'
            })
        assert get.status_code == 200
        g = get.json()
        assert g["tags"] == [f"{tag_name}"]

        # test DELETE request to verify new tag was deleted successfully from the vulnerability.
        delete = requests.delete(
            "https://ce.contrastsecurity.com/Contrast/api/ng/b72cd362-9374-40a1-a9b2-f4720b522874/tags/trace/2ASW-K5P0-LPPB-PQ36",
            headers={
                'Authorization': f'{settings.Contrast.AdminUser().auth}',
                'API-Key': f'{settings.Contrast.AdminUser().api_key}',
                'Content-Type': 'application/json'
            },
            json={"tag": f"{tag_name}"}
            )
        # test will fail on the line 42, status_code should be 200, this is to exercise bug report BR-006.
        assert delete.status_code == 201
        d = delete.json()
        assert d["messages"] == ["Tag deleted successfully"]

        # print statement to have a record of tag name in case you want to check it on the UI.
        print(tag_name)
