from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView 
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from apps.index.models import * 
from apps.index.forms import * 
from apps.users.forms import *


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class IndexView(TemplateView):
    template_name = "index.html"


# class Dashboard(TemplateView):
#     template_name = "dashboard.html"


# Aircraft Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListAircraft (ListView):
    template_name = 'aircraft/list.html'
    model = AirCraft
    context_object_name = 'aircraft_list'


def get_municipalities(request):
    id_department = request.GET.get('id_department')
    municipalities = Municipality.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_department:
        municipalities = Municipality.objects.filter(department__pk=id_department)   
    for municipality in municipalities:
        options += '<option value="%s">%s</option>' % (
            municipality.pk,
            municipality.name
        )
    response = {}
    response['municipalities'] = options
    return JsonResponse(response)


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateAircraft (CreateView):
    template_name = 'aircraft/form.html'
    model = AirCraft
    form = AirCraftForm
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['municipality'].queryset = Municipality.objects.none()
        context['departments'] = Department.objects.all()
        return context
    
    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aircraft', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailAircraft(DetailView):
    template_name ="aircraft/detail.html"
    model = AirCraft
    context_object_name = "property_list"


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateAircraft(UpdateView):
    template_name = "aircraft/form.html"
    model = AirCraft
    form = AirCraftForm
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'].fields['municipality'].queryset = Municipality.objects.filter(department=instance.municipality.department)
        context['departments'] = Department.objects.all()
        context['department_id'] = instance.municipality.department.pk
        return context
    
    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aircraft', kwargs={'pk': pk})
    

@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteAircraft (DeleteView):
    model = AirCraft
    success_url = reverse_lazy('index:list_aircraft')
# Aircraft Views


# Crew Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateCrew(CreateView):
    template_name = 'crew/create.html'
    model = Crew     
    form = CrewForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_crew', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailCrew(DetailView): 
    template_name= "crew/detail.html"
    model = Crew
    context_object_name = "crew_list" 


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateCrew(UpdateView):
    template_name="crew/create.html"
    model = Crew
    form = CrewForm
    fields = '__all__'
    
    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_crew', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteCrew(DeleteView):
    model = Crew
    success_url = reverse_lazy('index:list_crew')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListCrew(ListView):
    template_name = "crew/list.html"
    model = Crew
    context_object_name = "crew_list"
# Crew Views


# UOMA Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateUOMA(CreateView):
    template_name = 'uoma/create.html'
    model = MajorOperativeUnit
    form = MajorOperativeUnitForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_uoma', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailUOMA(DetailView): 
    template_name = "uoma/detail.html"
    model = MajorOperativeUnit


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateUOMA(UpdateView):
    template_name="uoma/create.html"
    model = MajorOperativeUnit
    form = MajorOperativeUnitForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_uoma', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteUOMA(DeleteView):
    model = MajorOperativeUnit
    success_url = reverse_lazy('index:list_uoma')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListUOMA(ListView):
    template_name = "uoma/list.html"
    model = MajorOperativeUnit
    context_object_name = "uoma_list"
# UOMA Views


# UOME Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateUOME(CreateView):
    template_name = 'uome/create.html'
    model = MinorOperativeUnit
    form = MinorOperativeUnitForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_uome', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailUOME(DetailView): 
    template_name = "uome/detail.html"
    model = MinorOperativeUnit


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateUOME(UpdateView):
    template_name="uome/create.html"
    model = MinorOperativeUnit
    form = MinorOperativeUnitForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_uome', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteUOME(DeleteView):
    model = MinorOperativeUnit
    success_url = reverse_lazy('index:list_uome')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListUOME(ListView):
    template_name = "uome/list.html"
    model = MinorOperativeUnit
    context_object_name = "uome_list"
# UOME Views


# Tactic Unit Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateTacticUnit(CreateView):
    template_name = 'tactic_unit/create.html'
    model = TacticUnit
    form = TacticUnitForm
    fields = '__all__'
    
    

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_tactic_unit', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailTacticUnit(DetailView): 
    template_name = "tactic_unit/detail.html"
    model = TacticUnit


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateTacticUnit(UpdateView):
    template_name="tactic_unit/create.html"
    model = TacticUnit
    form = TacticUnitForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_tactic_unit', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteTacticUnit(DeleteView):
    model = TacticUnit
    success_url = reverse_lazy('index:list_tactic_unit')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListTacticUnit(ListView):
    template_name = "tactic_unit/list.html"
    model = TacticUnit
    context_object_name = "ut_list"
# Tactic Unit Views

    
# Major Operation Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateMajorOperation(CreateView):
    template_name = 'major_operation/create.html'
    model = MajorOperation
    form = MajorOperationForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_major_operation', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailMajorOperation(DetailView): 
    template_name = "major_operation/detail.html"
    model = MajorOperation


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateMajorOperation(UpdateView):
    template_name="major_operation/create.html"
    model = MajorOperation
    form = MajorOperationForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_major_operation', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteMajorOperation(DeleteView):
    model = MajorOperation
    success_url = reverse_lazy('index:list_major_operation')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListMajorOperation(ListView):
    template_name = "major_operation/list.html"
    model = MajorOperation
    context_object_name = "major_operation_list"
# Major Operation Views  
    

# Operation Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateOperation(CreateView):
    template_name = 'operation/create.html'
    model = Operation
    form = OperationForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_operation', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailOperation(DetailView): 
    template_name = "operation/detail.html"
    model = Operation


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateOperation(UpdateView):
    template_name="operation/create.html"
    model = Operation
    form = OperationForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_operation', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteOperation(DeleteView):
    model = Operation
    success_url = reverse_lazy('index:list_operation')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListOperation(ListView):
    template_name = "operation/list.html"
    model = Operation
    context_object_name = "operation_list"
# Operation Views  


# FlightCondition Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateFlightCondition(CreateView):
    template_name = 'flight_condition/create.html'
    model = FlightCondition
    form = FlightConditionForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_flight_condition', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailFlightCondition(DetailView): 
    template_name = "flight_condition/detail.html"
    model = FlightCondition


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateFlightCondition(UpdateView):
    template_name="flight_condition/create.html"
    model = FlightCondition
    form = FlightConditionForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_flight_condition', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteFlightCondition(DeleteView):
    model = FlightCondition
    success_url = reverse_lazy('index:list_flight_condition')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListFlightCondition(ListView):
    template_name = "flight_condition/list.html"
    model = FlightCondition
    context_object_name = "flight_condition_list"
# FlightCondition Views 


# Agreement Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateAgreement(CreateView):
    template_name = 'agreement/create.html'
    model = Agreement
    form = AgreementForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_agreement', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailAgreement(DetailView): 
    template_name = "agreement/detail.html"
    model = Agreement


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateAgreement(UpdateView):
    template_name="agreement/create.html"
    model = Agreement
    form = AgreementForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_agreement', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteAgreement(DeleteView):
    model = Agreement
    success_url = reverse_lazy('index:list_agreement')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListAgreement(ListView):
    template_name = "agreement/list.html"
    model = Agreement
    context_object_name = "agreement_list"
# Agreement Views 


# AirCraftType Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateAirCraftType(CreateView):
    template_name = 'aircraft_type/create.html'
    model = AirCraftType
    form = AirCraftTypeForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aircraft_type', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailAirCraftType(DetailView): 
    template_name = "aircraft_type/detail.html"
    model = AirCraftType


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateAirCraftType(UpdateView):
    template_name="aircraft_type/create.html"
    model = AirCraftType
    form = AirCraftTypeForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aircraft_type', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteAirCraftType(DeleteView):
    model = AirCraftType
    success_url = reverse_lazy('index:list_aircraft_type')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListAirCraftType(ListView):
    template_name = "aircraft_type/list.html"
    model = AirCraftType
    context_object_name = "aircraft_type_list"
# AirCraftType Views 


# AirCraftModel Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateAirCraftModel(CreateView):
    template_name = 'aircraft_model/create.html'
    model = AirCraftModel
    form = AirCraftModelForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aircraft_model', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailAirCraftModel(DetailView): 
    template_name = "aircraft_model/detail.html"
    model = AirCraftModel


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateAirCraftModel(UpdateView):
    template_name="aircraft_model/create.html"
    model = AirCraftModel
    form = AirCraftModelForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aircraft_model', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteAirCraftModel(DeleteView):
    model = AirCraftModel
    success_url = reverse_lazy('index:list_aircraft_model')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListAirCraftModel(ListView):
    template_name = "aircraft_model/list.html"
    model = AirCraftModel
    context_object_name = "aircraft_model_list"
# AirCraftType Views 


# AviationEvent Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateAviationEvent(CreateView):
    template_name = 'aviation_event/create.html'
    model = AviationEvent
    form = AviationEventForm
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['municipality'].queryset = Municipality.objects.none()
        context['departments'] = Department.objects.all()
        return context

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aviation_event', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailAviationEvent(DetailView): 
    template_name = "aviation_event/detail.html"
    model = AviationEvent


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateAviationEvent(UpdateView):
    template_name="aviation_event/create.html"
    model = AviationEvent
    form = AviationEventForm
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'].fields['municipality'].queryset = Municipality.objects.filter(department=instance.municipality.department)
        context['departments'] = Department.objects.all()
        context['department_id'] = instance.municipality.department.pk
        return context

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aviation_event', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteAviationEvent(DeleteView):
    model = AviationEvent
    success_url = reverse_lazy('index:list_aviation_event')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListAviationEvent(ListView):
    template_name = "aviation_event/list.html"
    model = AviationEvent
    context_object_name = "aviation_event_list"
# AviationEvent Views 


# MissionType Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateMissionType(CreateView):
    template_name = 'mission_type/create.html'
    model = MissionType
    form = MissionTypeForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_mission_type', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailMissionType(DetailView): 
    template_name = "mission_type/detail.html"
    model = MissionType


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateMissionType(UpdateView):
    template_name="mission_type/create.html"
    model = MissionType
    form = MissionTypeForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_mission_type', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteMissionType(DeleteView):
    model = MissionType
    success_url = reverse_lazy('index:list_mission_type')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListMissionType(ListView):
    template_name = "mission_type/list.html"
    model = MissionType
    context_object_name = "mission_type_list"
# MissionType Views


# AviationMission Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateAviationMission(CreateView):
    template_name = 'aviation_mission/create.html'
    model = AviationMission
    form = AviationMissionForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aviation_mission', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailAviationMission(DetailView): 
    template_name = "aviation_mission/detail.html"
    model = AviationMission


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateAviationMission(UpdateView):
    template_name="aviation_mission/create.html"
    model = AviationMission
    form = AviationMissionForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_aviation_mission', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteAviationMission(DeleteView):
    model = AviationMission
    success_url = reverse_lazy('index:list_aviation_mission')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListAviationMission(ListView):
    template_name = "aviation_mission/list.html"
    model = AviationMission
    context_object_name = "aviation_mission_list"
# AviationMission Views 


# Configuration Views
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateConfiguration(CreateView):
    template_name = 'configuration/create.html'
    model = Configuration
    form = ConfigurationForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_configuration', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DetailConfiguration(DetailView): 
    template_name = "configuration/detail.html"
    model = Configuration


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateConfiguration(UpdateView):
    template_name="configuration/create.html"
    model = Configuration
    form = ConfigurationForm
    fields = '__all__'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:detail_configuration', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class DeleteConfiguration(DeleteView):
    model = Configuration
    success_url = reverse_lazy('index:list_configuration')


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListConfiguration(ListView):
    template_name = "configuration/list.html"
    model = Configuration
    context_object_name = "configuration_list"
# Configuration Views 


#Javi
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateFlightReport(CreateView):
    template_name = 'flight_report/create.html'
    model = FlightReport
    form = FlightReportForm
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['municipality'].queryset = Municipality.objects.none()
        context['departments'] = Department.objects.all()
        return context
   # def get_success_url(self):
     #   pk = self.object.pk
        #return reverse('index:detail_configuration', kwargs={'pk': pk})


def get_minor_operative_units(request):
    id_major_operative_unit = request.GET.get('id_major_operative_unit')
    minor_operative_units = MinorOperativeUnit.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_major_operative_unit:
        minor_operative_units = MinorOperativeUnit.objects.filter(major_operative_unit__pk=id_major_operative_unit)   
    for minor_operative_unit in minor_operative_units:
        options += '<option value="%s">%s</option>' % (
            minor_operative_unit.pk,
            minor_operative_unit.name
        )
    response = {}
    response['minor_operative_units'] = options
    return JsonResponse(response)        