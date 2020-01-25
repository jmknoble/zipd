"""Utility functions."""


def add_to_list(a_list, an_iterable, check=False):
    """
    Extend a list with the items from an iterable.

    :Args:
        a_list
            The list to extend

        an_iterable
            An iterable containing items to add to `a_list`

        check
            (optional) A value to inspect to determine whether to
            extend the list; the list is only extended if the value
            is not `None`

    :Returns:
        `a_list`, whether or not it was extended

    :Raises:
        See `list.extend()`:py:meth:
    """
    if check is not None:
        a_list.extend(an_iterable)
    return a_list


def dict_merge(*dicts):
    """
    Merge zero or more dict-ish objects in order and return the result.

    Keys in dictionaries later in the sequence take precedence over earlier
    ones.

    :Args:
        *dicts
            zero or more dictionaries provided as arguments

    :Returns:
        a single dictionary composed of keys from `dicts`

    :Raises:
        See `dict.update()`:py:meth:
    """
    result = {}
    for a_dict in dicts:
        result.update(a_dict)
    return result


def is_string(an_object):
    """
    Tell whether a given object refers to a string.

    We do this in a Python-version-indpendent way.

    :Args:
        an_object
            a given Python object

    :Returns:
        `True`-ish if `an_object` is a Python string, `False` otherwise
    """
    try:
        return isinstance(an_object, basestring)
    except NameError:  # Python 3: "NameError: name 'basestring' is not defined"
        return isinstance(an_object, str)


def starts_or_ends_with(target, value, caseless=False):
    """
    Tell whether `target` starts or ends with `value`.

    :Args:
        target
            the string to look in

        value
            the string to look for

        caseless
            (optional) If `True`-ish, force both `target` and `value` to
            lowercase before checking.

    :Returns:
        `True`-ish if `target` either starts or ends with `value` (see
        `caseless` arg above), `False`-ish otherwise

    :Raises:
        - `TypeError`:py:exc: if:
            - `target` has no `lower()`:py:meth:, `startswith()`:py:meth:, or
              `endswith()`:py:meth: method, or
            - `value` is an iterable and one or more of its items has no
              `lower()`:py:meth: method, or
            - `value` is not an iterable, `caseless` is `True`-ish, and `value`
              has no `lower()`:py:meth: method, or
            - `value` is neither a string nor an iterable containing strings
        - See `string.startswith()`:py:meth: and `string.endswith()`:py:meth:
          for other possible exceptions.
    """
    try:
        if caseless:
            target = target.lower()
            if is_string(value):
                value = value.lower()
            else:
                value = tuple(x.lower() for x in value)
        elif not is_string(value):
            value = tuple(x for x in value)
        result = target.startswith(value) or target.endswith(value)
    except AttributeError as e:
        raise TypeError(e)

    return result
