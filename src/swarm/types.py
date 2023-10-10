import enum


class ObjectType(enum.Enum):
    AGENT = "A"
    OBJECT = "O"
    FOOD = "F"
    HUB = "H"
    GENERIC = OBJECT
    NOTYPE = "X"

    @staticmethod
    def str2enum(item):
        item = item.lower()
        retval = ObjectType.GENERIC
        match item:
            case "food":
                retval = ObjectType.FOOD
            case "hub" | "base":
                retval = ObjectType.HUB
            case "agent":
                retval = ObjectType.AGENT
            case "generic":
                retval = ObjectType.GENERIC
            case _ :
                retval = ObjectType.NOTYPE

        return retval



    @staticmethod
    def enum2str(self, item, capitality="First"):
        raise  NotImplemented()