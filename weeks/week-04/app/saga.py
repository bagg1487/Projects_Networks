from enum import Enum

class State(str, Enum):
    NEW = "NEW"
    PAID = "PAID"
    DONE = "DONE"
    CANCELLED = "CANCELLED"

class Event(str, Enum):
    CREATE = "create"
    RESERVE_EMAIL = "reserve_email"
    PAY_OK = "PAY_OK"
    PAY_FAIL = "PAY_FAIL"  
    CREATE_USER = "create_user"
    FAIL = "fail"
    COMPENSATE = "compensate"
    RETRY = "retry"

def next_state(state: str, event: str) -> str:
    """
    Машина состояний для Saga пользователя
    """
    transitions = {
        (None, Event.CREATE): State.NEW,
        (State.NEW, Event.RESERVE_EMAIL): State.NEW,
        (State.NEW, Event.PAY_OK): State.PAID,
        (State.NEW, Event.PAY_FAIL): State.CANCELLED,  
        (State.NEW, Event.FAIL): State.CANCELLED,
        (State.NEW, Event.COMPENSATE): State.CANCELLED,
        (State.PAID, Event.CREATE_USER): State.DONE,
        (State.PAID, Event.FAIL): State.CANCELLED,
        (State.PAID, Event.COMPENSATE): State.CANCELLED,
        (State.CANCELLED, Event.RETRY): State.NEW,
    }
    
    next_state = transitions.get((state, event))
    
    if next_state is None:
        if event == Event.FAIL:
            return State.CANCELLED
        return state if state else State.CANCELLED
    
    return next_state.value if isinstance(next_state, State) else next_state