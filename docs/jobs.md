::: api.job
    handler: python
    members:
      - MergePytorchBins
    options:
      show_root_heading: true
      show_source: false
      show_bases : false
      heading_level : 5



# Job Schema
The job schema is a JSON object that defines the structure of a job. It contains the following fields:

| Field   | Type   | Required | Unique | Default | Options                     |
|---------|--------|----------|--------|---------|-----------------------------|
| id      | string | True     | True   |         |                             |
| name    | string | False    | False  |         |                             |
| user    | string | False    | False  |         |                             |
| request | string | False    | False  |         |                             |
| result  | string | False    | False  |         |                             |
| status  | string | False    | False  | idle    | idle, pending, running, finished, error |
| messages| string | False    | False  |         |                             |

## JSON Schema
``` json
{
    "id":{"type":"string", "required":True, "unique":True, "default": "","options":[]},
    "name":{"type":"string", "required":False, "unique":False, "default": "","options":[]},
    "user":{"type":"string", "required":False, "unique":False, "default": "","options":[]},
    "request":{"type":"string", "required":False, "unique":False, "default": "","options":[]},
    "result":{"type":"string", "required":False, "unique":False, "default": "","options":[]},
    "status":{"type":"string", "required":False, "unique":False, "default": "idle", "options":["idle","pending", "running", "finished", "error"]},
    "messages":{"type":"string", "required":False, "unique":False, "default": "","options":[]},
}
```