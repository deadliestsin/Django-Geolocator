from django.test import TestCase
from .models import Event, EventType
from django.contrib.gis.geos import GEOSGeometry

class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        EventType.objects.create(name='Tournament', description='Indoor Tournaments')
        eventType = EventType.objects.get(name='Tournament')
        Event.objects.create(name='Chess', location='POINT(10.1 11.2)', date=20190727, eventType = eventType)

    def test_event_name_test_date(self):
        event = Event.objects.get(eventType__name__icontains='tour')
        self.assertEquals(event.name, 'Chess')
        self.assertEquals(event.date, 20190727)

    def test_event_location_proximity(self):
        test_point = GEOSGeometry('POINT({lat} {lon})'.format(lat='10.1', lon='11.2'), srid=4326)
        point = GEOSGeometry('POINT({lat} {lon})'.format(lat='10.9', lon='11.9'), srid=4326)
        event = Event.objects.get(location__distance_lte=(point, 30000))
        self.assertEquals(event.location, test_point)

    def test_event_type(self):
        event = Event.objects.get(eventType__name__icontains='tour')
        eventType = EventType.objects.get(name='Tournament')
        self.assertEquals(event.eventType, eventType)

    def test_event_count(self):
        event = Event.objects.get(eventType__name__icontains='tour')
        eventType = EventType.objects.get(name='Tournament')
        self.assertEquals(event.eventType, eventType)