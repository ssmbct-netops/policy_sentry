#!/usr/bin/env python
from policy_sentry.shared.database import connect_db
from policy_sentry.querying.actions import get_actions_with_arn_type_and_access_level
import json

if __name__ == '__main__':
    db_session = connect_db('bundled')
    output = get_actions_with_arn_type_and_access_level(db_session, "ram", "resource-share", "Permissions management")
    print(json.dumps(output, indent=4))

"""
Output:

[
    'ram:associateresourceshare',
    'ram:createresourceshare',
    'ram:deleteresourceshare',
    'ram:disassociateresourceshare',
    'ram:updateresourceshare'
]
"""
