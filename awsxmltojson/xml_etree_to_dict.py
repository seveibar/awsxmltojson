from .get_shape import get_shape
import logging

logger = logging.getLogger(__name__)


def xml_etree_to_dict(elm, shape=None, level=1):
    shape = shape or get_shape(elm.tag)
    logger.debug(">" * level, elm.tag, shape)
    if shape is None:
        d = {}
        for child in elm:
            child_d = xml_etree_to_dict(child, level=level + 1)
            d.update(child_d)
        return {elm.tag: d}

    if shape == "String":
        return elm.text

    if shape["type"] == "structure":
        d = {}
        for member_name, member_metadata in shape["members"].items():
            member_shape = get_shape(member_metadata["shape"])
            logger.debug(">" * level + "(m)", member_name, member_shape)
            if member_shape["type"] == "list":
                # we lowercase the first letter for lists by AWS Accept: application/json convention
                list_key = member_name[0].lower() + member_name[1:]
                d[list_key] = []
                for child in elm:
                    if child.tag == member_shape["member"]["locationName"]:
                        d[list_key].append(xml_etree_to_dict(child, level=level + 1))
            elif member_shape["type"] == "string":
                try:
                    d[member_name] = elm.find(member_name).text.strip()
                except AttributeError:
                    pass
            elif member_shape["type"] == "map":
                if "locationName" not in member_shape:
                    continue
                map_elms = elm.findall(member_shape["locationName"])
                for map_elm in map_elms:
                    key = map_elm.find(member_shape["key"]["locationName"]).text
                    val_elm = map_elm.find(member_shape["value"]["locationName"])
                    d[key] = xml_etree_to_dict(
                        val_elm, shape=member_shape["value"]["shape"], level=level + 1
                    )
            else:
                raise Exception(
                    f'Unknown shape type "{member_shape["type"]}" for {member_name}'
                )
        return d
    return {}