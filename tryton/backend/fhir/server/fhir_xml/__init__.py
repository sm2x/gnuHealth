from .support_functions import *
from .config import *
import sys
from .base_classes import *

GDSClassesMapping = {
    'code': Coding,
    'chain': string,
    'issued': instant,
    'actionResulting': ResourceReference,
    'concern': ResourceReference,
    'focus': code,
    'prefix': string,
    'valueAttachment': Attachment,
    'assessment': ResourceReference,
    'query': base64Binary,
    'issuer': ResourceReference,
    'valueIdentifier': Identifier,
    'compose': ValueSet_Compose,
    'exampleUri': uri,
    'equivalence': ConceptMapEquivalence,
    'referenceResource': ResourceReference,
    'bornPeriod': Period,
    'exampleRatio': Ratio,
    'ingredient': Substance_Ingredient,
    'lowerLimit': decimal,
    'dispense': Supply_Dispense,
    'sopclass': oid,
    'reasonResource': ResourceReference,
    'choice': Coding,
    'refusedIndicator': boolean,
    'maxLength': integer,
    'dischargeDiagnosis': ResourceReference,
    'encounter': ResourceReference,
    'reAdmission': boolean,
    'exampleSchedule': Schedule,
    'gender': CodeableConcept,
    'notes': string,
    'additionalInstructions': CodeableConcept,
    'item': ResourceReference,
    'valueRatio': Ratio,
    'answerString': string,
    'requirements': string,
    'numberOfInstances': integer,
    'dataInstant': instant,
    'rate': Ratio,
    'asNeededCodeableConcept': CodeableConcept,
    'dataAttachment': Attachment,
    'section': Composition_Section,
    'version': string,
    'emptyReason': CodeableConcept,
    'nameReference': string,
    'supplier': ResourceReference,
    'method': CodeableConcept,
    'valueString': string,
    'hash': string,
    'relatesTo': DocumentReference_RelatesTo,
    'doseQuantity': Quantity,
    'reported': boolean,
    'dataHumanName': HumanName,
    'address': Address,
    'active': boolean,
    'presentedForm': Attachment,
    'documentMailbox': uri,
    'dataId': id,
    'publisher': string,
    'substance': ResourceReference,
    'remarks': string,
    'amount': Quantity,
    'action': SecurityEventAction,
    'options': ResourceReference,
    'answerDate': date,
    'dateAsserted': date,
    'multipleBirthInteger': integer,
    'diagnosticDateTime': dateTime,
    'confidentiality': CodeableConcept,
    'family': string,
    'clinicalNotes': string,
    'codedDiagnosis': CodeableConcept,
    'exampleDate': date,
    'dataOid': oid,
    'exampleString': string,
    'total': integer,
    'use': NameUse,
    'reasonNotGiven': CodeableConcept,
    'zip': string,
    'destination': ResourceReference,
    'outcomeDesc': string,
    'maxDosePerPeriod': Ratio,
    'next': Extension,
    'exampleOid': oid,
    'answerDecimal': decimal,
    'extensionDefn': Profile_ExtensionDefn,
    'stage': Condition_Stage,
    'type': CodeableConcept,
    'dataUri': uri,
    'valueUri': uri,
    'relatedItem': Procedure_RelatedItem,
    'flag': CodeableConcept,
    'lotNumber': string,
    'exampleDateTime': dateTime,
    'valueDateTime': dateTime,
    'op': FilterOperator,
    'endpoint': uri,
    'policyManager': uri,
    'constraint': Profile_Constraint,
    'modified': dateTime,
    'longitude': decimal,
    'dosage': MedicationStatement_Dosage,
    'performer': Procedure_Performer,
    'abatementAge': Age,
    'orderedItem': ResourceReference,
    'agent': Provenance_Agent,
    'high': Quantity,
    'timingDateTime': dateTime,
    'expirationDate': date,
    'fulfillment': ResourceReference,
    'whenGiven': Period,
    'exclude': ValueSet_Include,
    'species': CodeableConcept,
    'suppliedItem': ResourceReference,
    'concept': ValueSet_Concept,
    'modifierExtension': Extension,
    'end': dateTime,
    'goal': CarePlan_Goal,
    'dataInteger': integer,
    'attachment': ResourceReference,
    'doseTarget': CodeableConcept,
    'parameter': Extension,
    'profile': uri,
    'map': string,
    'product': Medication_Product,
    'description': string,
    'dataIdentifier': Identifier,
    'max': string,
    'mapping': Profile_Mapping1,
    'collection': Specimen_Collection,
    'accessionIdentifier': Identifier,
    'date': dateTime,
    'participant': SecurityEvent_Participant,
    'data': ResourceReference,
    'response': Query_Response,
    'organization': ResourceReference,
    'object': SecurityEvent_Object,
    'documentation': string,
    'element': Profile_Element,
    'representation': PropertyRepresentation,
    'valueUuid': uuid,
    'order': ResourceReference,
    'origin': ResourceReference,
    'interpretation': CodeableConcept,
    'dataCoding': Coding,
    'telecom': Contact,
    'dataPeriod': Period,
    'userId': string,
    'entity': Provenance_Entity,
    'releaseDate': dateTime,
    'report': ResourceReference,
    'appliesPeriod': Period,
    'valueAddress': Address,
    'valueCodeableConcept': CodeableConcept,
    'group': Questionnaire_Group,
    'searchInclude': string,
    'valueBoolean': boolean,
    'latitude': decimal,
    'conformance': BindingConformance,
    'dataSchedule': Schedule,
    'animal': Patient_Animal,
    'specialCourtesy': CodeableConcept,
    'timestamp': instant,
    'primary': boolean,
    'valueRange': Range,
    'requestDetail': ResourceReference,
    'accomodation': Encounter_Accomodation,
    'valueId': id,
    'name': string,
    'clinicalInformation': string,
    'referrer': ResourceReference,
    'exampleResource': ResourceReference,
    'mode': LocationMode,
    'dependsOn': ConceptMap_DependsOn,
    'identifier': Identifier,
    'upperLimit': decimal,
    'series': string,
    'deceasedDate': date,
    'frames': integer,
    'frequency': integer,
    'exampleContact': Contact,
    'operation': Conformance_Operation,
    'collector': ResourceReference,
    'event': SecurityEvent_Event,
    'category': MessageSignificanceCategory,
    'managingOrganization': ResourceReference,
    'container': Specimen_Container,
    'network': SecurityEvent_Network,
    'dataCodeableConcept': CodeableConcept,
    'publish': boolean,
    'content': Medication_Content,
    'dataSampledData': SampledData,
    'contained': Resource_Inline,
    'issue': OperationOutcome_Issue,
    'model': string,
    'valueContact': Contact,
    'reason': CodeableConcept,
    'seriesDoses': integer,
    'definition': string,
    'language': code,
    'created': date,
    'route': CodeableConcept,
    'filter': ValueSet_Filter,
    'length': integer,
    'qualification': Practitioner_Qualification,
    'first': Extension,
    'onsetDate': date,
    'suffix': string,
    'isExtensible': boolean,
    'coding': Coding,
    'number': integer,
    'bodySite': CodeableConcept,
    'owner': ResourceReference,
    'discriminator': id,
    'size': integer,
    'city': string,
    'given': string,
    'service': DocumentReference_Service,
    'width': integer,
    'breed': CodeableConcept,
    'system': uri,
    'lifecycle': SecurityEventObjectLifecycle,
    'priority': CodeableConcept,
    'isModifier': boolean,
    'sensitivity': CodeableConcept,
    'relationship': HierarchicalRelationshipType,
    'masterIdentifier': Identifier,
    'explanation': Immunization_Explanation,
    'answerInstant': instant,
    'short': string,
    'authorityResource': ResourceReference,
    'udi': string,
    'symptom': AdverseReaction_Symptom,
    'exampleCoding': Coding,
    'kind': CodeableConcept,
    'target': ResourceReference,
    'bed': ResourceReference,
    'dispenser': ResourceReference,
    'outcome': SecurityEventOutcome,
    'valueBase64Binary': base64Binary,
    'mimeType': code,
    'dataBase64Binary': base64Binary,
    'timingPeriod': Period,
    'caseSensitive': boolean,
    'exampleRange': Range,
    'timingSchedule': Schedule,
    'modality': Modality,
    'dailyAmount': Quantity,
    'dataRange': Range,
    'min': integer,
    'responsible': ResourceReference,
    'note': string,
    'instance': Substance_Instance,
    'answerDateTime': dateTime,
    'indexed': instant,
    'facilityType': CodeableConcept,
    'channel': DeviceObservationReport_Channel,
    'validityPeriod': Period,
    'fhirVersion': id,
    'dataCode': code,
    'denominator': Quantity,
    'vaccinationProtocol': Immunization_VaccinationProtocol,
    'position': Location_Position,
    'device': ResourceReference,
    'class': EncounterClass,
    'answerInteger': integer,
    'collectedDateTime': dateTime,
    'synonym': string,
    'observation': ResourceReference,
    'url': uri,
    'attester': Composition_Attester,
    'request': ResourceReference,
    'quantity': Quantity,
    'exampleQuantity': Quantity,
    'refusalReason': CodeableConcept,
    'text': string,
    'supercedes': ResourceReference,
    'isBrand': boolean,
    'relation': FamilyHistory_Relation,
    'dataDate': date,
    'availability': InstanceAvailability,
    'accessionNo': Identifier,
    'admitSource': CodeableConcept,
    'deceasedDateTime': dateTime,
    'copyright': string,
    'title': string,
    'implementation': Conformance_Implementation,
    'valueCode': code,
    'factor': decimal,
    'diagnosticPeriod': Period,
    'doseStatus': CodeableConcept,
    'contentType': code,
    'custodian': ResourceReference,
    'exampleBoolean': boolean,
    'recordedDate': dateTime,
    'timing': Schedule,
    'wasNotGiven': boolean,
    'resource': Conformance_Resource,
    'dataString': string,
    'dateCriterion': ImmunizationRecommendation_DateCriterion,
    'summary': CodeableConcept,
    'subtype': CodeableConcept,
    'activity': CarePlan_Activity,
    'view': CodeableConcept,
    'reference': ResourceReference,
    'exampleAttachment': Attachment,
    'individual': ResourceReference,
    'result': ResourceReference,
    'interpreter': ResourceReference,
    'updateCreate': boolean,
    'primaryLanguage': code,
    'subject': ResourceReference,
    'followUp': string,
    'exampleSampledData': SampledData,
    'capacity': Quantity,
    'expectedSupplyDuration': Duration,
    'label': string,
    'state': string,
    'dataAddress': Address,
    'multipleBirthBoolean': boolean,
    'import': uri,
    'exampleInstant': instant,
    'valueHumanName': HumanName,
    'exampleDecimal': decimal,
    'valueDate': date,
    'valueSampledData': SampledData,
    'reaction': Immunization_Reaction,
    'whenPrepared': Period,
    'prescription': ResourceReference,
    'country': string,
    'responsibleParty': ResourceReference,
    'context': string,
    'receiver': ResourceReference,
    'experimental': boolean,
    'comment': string,
    'exampleUuid': uuid,
    'key': id,
    'simple': CarePlan_Simple,
    'dataContact': Contact,
    'valueDecimal': decimal,
    'period': Period,
    'birthDate': dateTime,
    'height': integer,
    'header': string,
    'onsetRange': Range,
    'path': string,
    'exampleAddress': Address,
    'onsetString': string,
    'abatementDate': date,
    'exposure': AdverseReaction_Exposure,
    'requestor': boolean,
    'enterer': ResourceReference,
    'didNotOccurFlag': boolean,
    'location': ResourceReference,
    'collectedPeriod': Period,
    'sensitivityTest': ResourceReference,
    'hospitalization': Encounter_Hospitalization,
    'policy': uri,
    'treatment': Specimen_Treatment,
    'last': Extension,
    'exampleCode': code,
    'valuePeriod': Period,
    'comparator': QuantityCompararator,
    'value': code,
    'deceasedBoolean': boolean,
    'contextType': ExtensionContext,
    'dischargeDisposition': CodeableConcept,
    'property': code,
    'procedure': CodeableConcept,
    'serviceCategory': CodeableConcept,
    'dataResource': ResourceReference,
    'causalityExpectation': CausalityExpectation,
    'metric': DeviceObservationReport_Metric,
    'binding': Profile_Binding,
    'site': string,
    'numberOfSeries': integer,
    'valueResource': ResourceReference,
    'asNeededBoolean': boolean,
    'reasonCodeableConcept': CodeableConcept,
    'bornString': string,
    'severity': ConstraintSeverity,
    'author': ResourceReference,
    'media': Coding,
    'authorizingPrescription': ResourceReference,
    'member': ResourceReference,
    'rules': SlicingRules,
    'units': UnitsOfTime,
    'party': ResourceReference,
    'document': Conformance_Document,
    'status': ValueSetStatus,
    'practitioner': ResourceReference,
    'purpose': string,
    'identity': id,
    'slicing': Profile_Slicing,
    'forecastStatus': CodeableConcept,
    'imagingStudy': ResourceReference,
    'dataDecimal': decimal,
    'person': ResourceReference,
    'contact': Patient_Contact,
    'extensible': boolean,
    'prescriber': ResourceReference,
    'doseSequence': integer,
    'entry': List_Entry,
    'vaccineType': CodeableConcept,
    'maritalStatus': CodeableConcept,
    'protocol': ImmunizationRecommendation_Protocol,
    'assigner': ResourceReference,
    'genderStatus': CodeableConcept,
    'photo': Attachment,
    'dateWritten': dateTime,
    'rest': Conformance_Rest,
    'human': string,
    'onsetAge': Age,
    'previous': Extension,
    'bornDate': date,
    'exampleCodeableConcept': CodeableConcept,
    'deceasedString': string,
    'source': Specimen_Source,
    'blob': base64Binary,
    'valueCoding': Coding,
    'criticality': Criticality,
    'format': uri,
    'authorityCodeableConcept': CodeableConcept,
    'serviceProvider': ResourceReference,
    'specimen': ResourceReference,
    'aggregation': AggregationMode,
    'asserter': ResourceReference,
    'recipient': ResourceReference,
    'preAdmissionIdentifier': Identifier,
    'doseNumber': integer,
    'formal': string,
    'referenceUri': uri,
    'substitution': MedicationPrescription_Substitution,
    'dateTime': instant,
    'referenceRange': Observation_ReferenceRange,
    'indication': CodeableConcept,
    'security': Conformance_Security,
    'deviceName': string,
    'deceasedAge': Age,
    'valueSet': ResourceReference,
    'authority': ResourceReference,
    'include': ValueSet_Include,
    'recommendation': ImmunizationRecommendation_Recommendation,
    'duration': decimal,
    'dataRatio': Ratio,
    'dimensions': integer,
    'altId': string,
    'recorded': instant,
    'comments': string,
    'recorder': ResourceReference,
    'answerBoolean': boolean,
    'valueSchedule': Schedule,
    'who': ResourceReference,
    'patient': ResourceReference,
    'schedule': Schedule,
    'deleted': boolean,
    'specialArrangement': CodeableConcept,
    'complication': CodeableConcept,
    'expansion': ValueSet_Expansion,
    'expiry': dateTime,
    'whenHandedOver': Period,
    'prohibited': boolean,
    'specimenQuantity': Quantity,
    'exampleInteger': integer,
    'cors': boolean,
    'additive': ResourceReference,
    'manufacturer': ResourceReference,
    'exampleBase64Binary': base64Binary,
    'actual': boolean,
    'certificate': Conformance_Certificate,
    'extension': Extension,
    'package': Medication_Package,
    'dataBoolean': boolean,
    'certainty': CodeableConcept,
    'numerator': Quantity,
    'numberOfRepeatsAllowed': integer,
    'valueQuantity': Quantity,
    'messaging': Conformance_Messaging,
    'software': string,
    'contains': ValueSet_Contains,
    'communication': CodeableConcept,
    'image': DiagnosticReport_Image,
    'readHistory': boolean,
    'exampleId': id,
    'operator': ResourceReference,
    'altitude': decimal,
    'question': Questionnaire_Question,
    'start': dateTime,
    'integritySignature': string,
    'low': Quantity,
    'acceptUnknown': boolean,
    'authored': dateTime,
    'xpath': string,
    'form': CodeableConcept,
    'specialty': CodeableConcept,
    'authenticator': ResourceReference,
    'link': Patient_Link,
    'related': Observation_Related,
    'docStatus': CodeableConcept,
    'line': string,
    'count': integer,
    'careProvider': ResourceReference,
    'characteristic': Group_Characteristic,
    'valueInstant': instant,
    'dosageInstruction': MedicationPrescription_DosageInstruction,
    'reliableCache': integer,
    'searchParam': Profile_SearchParam,
    'mustSupport': boolean,
    'define': ValueSet_Define,
    'display': string,
    'partOf': ResourceReference,
    'dataUuid': uuid,
    'medication': ResourceReference,
    'ordered': boolean,
    'uid': oid,
    'abstract': boolean,
    'condition': id,
    'exampleIdentifier': Identifier,
    'evidence': Condition_Evidence,
    'supportingPatientInformation': ResourceReference,
    'deceasedRange': Range,
    'orderer': ResourceReference,
    'reliability': ObservationReliability,
    'exampleHumanName': HumanName,
    'valueOid': oid,
    'virtualDevice': DeviceObservationReport_VirtualDevice,
    'when': Order_When,
    'detail': SecurityEvent_Detail,
    'actor': ResourceReference,
    'other': ResourceReference,
    'role': SecurityEventObjectRole,
    'details': string,
    'appliesDateTime': dateTime,
    'conclusion': string,
    'examplePeriod': Period,
    'repeat': Schedule_Repeat,
    'valueInteger': integer,
    'diet': CodeableConcept,
    'meaning': CodeableConcept,
    'dataQuantity': Quantity,
    'requester': ResourceReference,
    'abatementBoolean': boolean,
    'timingString': string,
    'structure': Profile_Structure,
    'supportingImmunization': ResourceReference,
    'physicalType': CodeableConcept,
    'sensitivityType': SensitivityType,
    'age': Range,
    'sourceSite': CodeableConcept,
    'doseStatusReason': CodeableConcept,
    'dataDateTime': dateTime,
    'time': dateTime,
    'receivedTime': dateTime,
}


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName, silence=False):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Element'
        rootClass = Element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFileName, silence=False):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Element'
        rootClass = Element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from io import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Element'
        rootClass = Element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFileName, silence=False):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Element'
        rootClass = Element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from fhirBase import *\n\n')
        sys.stdout.write('import fhirBase as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj

__all__ = [
    "Address",
    "AddressUse",
    "AdverseReaction",
    "AdverseReaction_Exposure",
    "AdverseReaction_Symptom",
    "Age",
    "AggregationMode",
    "Alert",
    "AlertStatus",
    "AllergyIntolerance",
    "Attachment",
    "BackboneElement",
    "Binary",
    "BindingConformance",
    "Block",
    "CarePlan",
    "CarePlanActivityCategory",
    "CarePlanActivityStatus",
    "CarePlanGoalStatus",
    "CarePlanStatus",
    "CarePlan_Activity",
    "CarePlan_Goal",
    "CarePlan_Participant",
    "CarePlan_Simple",
    "CausalityExpectation",
    "CodeableConcept",
    "Coding",
    "Composition",
    "CompositionAttestationMode",
    "CompositionStatus",
    "Composition_Attester",
    "Composition_Event",
    "Composition_Section",
    "ConceptMap",
    "ConceptMapEquivalence",
    "ConceptMap_Concept",
    "ConceptMap_DependsOn",
    "ConceptMap_Map",
    "Condition",
    "ConditionRelationshipType",
    "ConditionStatus",
    "Condition_Evidence",
    "Condition_Location",
    "Condition_RelatedItem",
    "Condition_Stage",
    "Conformance",
    "ConformanceEventMode",
    "ConformanceStatementStatus",
    "Conformance_Certificate",
    "Conformance_Document",
    "Conformance_Event",
    "Conformance_Implementation",
    "Conformance_Messaging",
    "Conformance_Operation",
    "Conformance_Operation1",
    "Conformance_Query",
    "Conformance_Resource",
    "Conformance_Rest",
    "Conformance_SearchParam",
    "Conformance_Security",
    "Conformance_Software",
    "ConstraintSeverity",
    "Contact",
    "ContactSystem",
    "ContactUse",
    "Count",
    "Criticality",
    "Device",
    "DeviceObservationReport",
    "DeviceObservationReport_Channel",
    "DeviceObservationReport_Metric",
    "DeviceObservationReport_VirtualDevice",
    "DiagnosticOrder",
    "DiagnosticOrderPriority",
    "DiagnosticOrderStatus",
    "DiagnosticOrder_Event",
    "DiagnosticOrder_Item",
    "DiagnosticReport",
    "DiagnosticReportStatus",
    "DiagnosticReport_Image",
    "Distance",
    "DocumentManifest",
    "DocumentMode",
    "DocumentReference",
    "DocumentReferenceStatus",
    "DocumentReference_Context",
    "DocumentReference_Parameter",
    "DocumentReference_RelatesTo",
    "DocumentReference_Service",
    "DocumentRelationshipType",
    "Duration",
    "Element",
    "Encounter",
    "EncounterClass",
    "EncounterState",
    "Encounter_Accomodation",
    "Encounter_Hospitalization",
    "Encounter_Location",
    "Encounter_Participant",
    "EventTiming",
    "ExposureType",
    "Extension",
    "ExtensionContext",
    "FamilyHistory",
    "FamilyHistory_Condition",
    "FamilyHistory_Relation",
    "FilterOperator",
    "Flow",
    "Group",
    "GroupType",
    "Group_Characteristic",
    "HierarchicalRelationshipType",
    "HumanName",
    "Identifier",
    "IdentifierUse",
    "ImagingModality",
    "ImagingStudy",
    "ImagingStudy_Instance",
    "ImagingStudy_Series",
    "Immunization",
    "ImmunizationRecommendation",
    "ImmunizationRecommendation_DateCriterion",
    "ImmunizationRecommendation_Protocol",
    "ImmunizationRecommendation_Recommendation",
    "Immunization_Explanation",
    "Immunization_Reaction",
    "Immunization_VaccinationProtocol",
    "Inline",
    "InstanceAvailability",
    "IssueSeverity",
    "LinkType",
    "List",
    "ListMode",
    "List_Entry",
    "Location",
    "LocationMode",
    "LocationStatus",
    "Location_Position",
    "Media",
    "MediaType",
    "Medication",
    "MedicationAdministration",
    "MedicationAdministrationStatus",
    "MedicationAdministration_Dosage",
    "MedicationDispense",
    "MedicationDispenseStatus",
    "MedicationDispense_Dispense",
    "MedicationDispense_Dosage",
    "MedicationDispense_Substitution",
    "MedicationKind",
    "MedicationPrescription",
    "MedicationPrescriptionStatus",
    "MedicationPrescription_Dispense",
    "MedicationPrescription_DosageInstruction",
    "MedicationPrescription_Substitution",
    "MedicationStatement",
    "MedicationStatement_Dosage",
    "Medication_Content",
    "Medication_Ingredient",
    "Medication_Package",
    "Medication_Product",
    "MessageHeader",
    "MessageHeader_Destination",
    "MessageHeader_Response",
    "MessageHeader_Source",
    "MessageSignificanceCategory",
    "Modality",
    "Money",
    "NameUse",
    "Narrative",
    "NarrativeStatus",
    "Observation",
    "ObservationRelationshipType",
    "ObservationReliability",
    "ObservationStatus",
    "Observation_ReferenceRange",
    "Observation_Related",
    "OperationOutcome",
    "OperationOutcome_Issue",
    "Order",
    "OrderOutcomeStatus",
    "OrderResponse",
    "Order_When",
    "Organization",
    "Organization_Contact",
    "Other",
    "Patient",
    "Patient_Animal",
    "Patient_Contact",
    "Patient_Link",
    "Period",
    "Practitioner",
    "Practitioner_Qualification",
    "Procedure",
    "ProcedureRelationshipType",
    "Procedure_Performer",
    "Procedure_RelatedItem",
    "Profile",
    "Profile_Binding",
    "Profile_Constraint",
    "Profile_Definition",
    "Profile_Element",
    "Profile_ExtensionDefn",
    "Profile_Mapping",
    "Profile_Mapping1",
    "Profile_Query",
    "Profile_SearchParam",
    "Profile_Slicing",
    "Profile_Structure",
    "Profile_Type",
    "PropertyRepresentation",
    "Provenance",
    "ProvenanceEntityRole",
    "Provenance_Agent",
    "Provenance_Entity",
    "Quantity",
    "QuantityCompararator",
    "Query",
    "QueryOutcome",
    "Query_Response",
    "Questionnaire",
    "QuestionnaireStatus",
    "Questionnaire_Group",
    "Questionnaire_Question",
    "Range",
    "Ratio",
    "ReactionSeverity",
    "RelatedPerson",
    "Resource",
    "ResourceProfileStatus",
    "ResourceReference",
    "Resource_Inline",
    "ResponseType",
    "RestfulConformanceMode",
    "RestfulOperationSystem",
    "RestfulOperationType",
    "SampledData",
    "SampledDataDataType",
    "Schedule",
    "Schedule_Repeat",
    "SearchParamType",
    "SecurityEvent",
    "SecurityEventAction",
    "SecurityEventObjectLifecycle",
    "SecurityEventObjectRole",
    "SecurityEventObjectType",
    "SecurityEventOutcome",
    "SecurityEventParticipantNetworkType",
    "SecurityEvent_Detail",
    "SecurityEvent_Event",
    "SecurityEvent_Network",
    "SecurityEvent_Object",
    "SecurityEvent_Participant",
    "SecurityEvent_Source",
    "SensitivityStatus",
    "SensitivityType",
    "SlicingRules",
    "Specimen",
    "Specimen_Collection",
    "Specimen_Container",
    "Specimen_Source",
    "Specimen_Treatment",
    "Substance",
    "Substance_Ingredient",
    "Substance_Instance",
    "Supply",
    "SupplyDispenseStatus",
    "SupplyStatus",
    "Supply_Dispense",
    "UnitsOfTime",
    "ValueSet",
    "ValueSetStatus",
    "ValueSet_Compose",
    "ValueSet_Concept",
    "ValueSet_Contains",
    "ValueSet_Define",
    "ValueSet_Expansion",
    "ValueSet_Filter",
    "ValueSet_Include",
    "a",
    "a_content",
    "abbr",
    "acronym",
    "area",
    "b",
    "base64Binary",
    "bdo",
    "big",
    "blockquote",
    "boolean",
    "br",
    "caption",
    "cite",
    "code",
    "col",
    "colgroup",
    "date",
    "dateTime",
    "dd",
    "decimal",
    "dfn",
    "div",
    "dl",
    "dt",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "i",
    "id",
    "img",
    "instant",
    "integer",
    "kbd",
    "li",
    "map",
    "oid",
    "ol",
    "p",
    "pre",
    "pre_content",
    "q",
    "samp",
    "small",
    "span",
    "string",
    "strong",
    "sub",
    "sup",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "tt",
    "ul",
    "uri",
    "uuid",
    "var"
]
