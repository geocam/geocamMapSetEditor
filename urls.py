# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from django.conf.urls.defaults import *  # pylint: disable=W0401
from django.conf import settings

urlpatterns = patterns(
    '',
    
    (r'^geocamMapSet/', include('geocamMapSet.urls')),
    (r'^mix/', include('mapMixerApp.urls')),
    
    )
