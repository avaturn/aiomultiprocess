# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

import multiprocessing
from asyncio import BaseEventLoop
from typing import (
    Any,
    AsyncContextManager,
    Callable,
    Dict,
    NamedTuple,
    NewType,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)

T = TypeVar("T")
R = TypeVar("R")

Context = multiprocessing.context.BaseContext
Queue = multiprocessing.Queue

TaskID = NewType("TaskID", int)
QueueID = NewType("QueueID", int)

TracebackStr = str

LoopInitializer = Callable[..., BaseEventLoop]
PoolTask = Optional[Tuple[TaskID, Callable[..., R], Sequence[T], Dict[str, T]]]
PoolResult = Tuple[TaskID, Optional[R], Optional[TracebackStr]]
Lifespan = Callable[[None], AsyncContextManager[None]]


class Unit(NamedTuple):
    """Container for what to call on the child process."""

    target: Callable
    args: Sequence[Any]
    kwargs: Dict[str, Any]
    namespace: Any
    initializer: Optional[Union[Lifespan, Callable]] = None
    initargs: Sequence[Any] = ()
    loop_initializer: Optional[LoopInitializer] = None
    runner: Optional[Callable] = None


class ProxyException(Exception):
    pass
