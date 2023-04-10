import copy

try:
    import ansible
except ImportError:
    ansible_available = False
else:
    ansible_available = True

if ansible_available:
    from ansible.errors import AnsibleFilterError


def full_secret_path(extra_path, current_path):

    extra_path_elements = extra_path.split('/') if extra_path else []

    result = [''] + current_path.copy()

    for index, extra_path_element in enumerate(extra_path_elements):
        if extra_path_element == '':
            if index == 0:
                result = []
            elif index != len(extra_path_elements) - 1:
                continue
        if extra_path_element != '.':
            result.append(extra_path_element)

    result = ['', ''] if result == [''] else result

    return '/'.join(result)


def full_secret_path_in_policy(policy, current_path):

    modified_policy = copy.deepcopy(policy)

    for rule in modified_policy['rules']:
        rule['path'] = full_secret_path(rule['path'], current_path)

    return modified_policy


class FilterModule(object):
    def filters(self):
        return {
            'full_secret_path': full_secret_path,
            'full_secret_path_in_policy': full_secret_path_in_policy
        }
