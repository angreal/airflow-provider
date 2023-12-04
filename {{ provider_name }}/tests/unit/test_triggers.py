from {{provider_slug}}.triggers import {{name | title | replace(from=" ", to="")}}Trigger

import pytest
import asyncio

def test_trigger():

    trigger = {{name | title | replace(from=" ", to="")}}Trigger()

    assert isinstance(trigger,{{name | title | replace(from=" ", to="")}}Trigger)

    classpath, kwargs = trigger.serialize()


@pytest.mark.asyncio
async def test_trigger_run_good(mocker):

    trigger = {{name | title | replace(from=" ", to="")}}Trigger()

    mocked_rv = {}
    mocker.patch.object( Object, "method", return_value = mocked_rv) # mock whatever return you need to make your trigger return from deferred state

    task = asyncio.create_task(trigger.run().__anext__())
    await asyncio.sleep(1.0)
    assert task.done() is True
    asyncio.get_event_loop().stop()
    


@pytest.mark.asyncio
async def test_trigger_run_bad(mocker):

    trigger2 = {{name | title | replace(from=" ", to="")}}Trigger()

    mocked_rv = {}
    mocker.patch.object( Object, "method", return_value = mocked_rv) # mock whatever return you need to make your trigger return from deferred state

    task2 = asyncio.create_task(trigger2.run().__anext__())
    await asyncio.sleep(1.0)
    assert task2.done() is False
    asyncio.get_event_loop().stop()