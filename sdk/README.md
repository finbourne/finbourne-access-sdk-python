<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fbn-prd.lusid.com/access*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationMetadataApi* | [**list_access_controlled_resources**](docs/ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control
*PoliciesApi* | [**add_to_policy_collection**](docs/PoliciesApi.md#add_to_policy_collection) | **POST** /api/policycollections/{code}/add | AddToPolicyCollection: Add To PolicyCollection
*PoliciesApi* | [**create_policy**](docs/PoliciesApi.md#create_policy) | **POST** /api/policies | CreatePolicy: Create Policy
*PoliciesApi* | [**create_policy_collection**](docs/PoliciesApi.md#create_policy_collection) | **POST** /api/policycollections | CreatePolicyCollection: Create PolicyCollection
*PoliciesApi* | [**delete_policy**](docs/PoliciesApi.md#delete_policy) | **DELETE** /api/policies/{code} | DeletePolicy: Delete Policy
*PoliciesApi* | [**delete_policy_collection**](docs/PoliciesApi.md#delete_policy_collection) | **DELETE** /api/policycollections/{code} | DeletePolicyCollection: Delete PolicyCollection
*PoliciesApi* | [**evaluate**](docs/PoliciesApi.md#evaluate) | **POST** /api/me | Evaluate: Run one or more evaluations
*PoliciesApi* | [**get_own_policies**](docs/PoliciesApi.md#get_own_policies) | **GET** /api/me | GetOwnPolicies: Get policies of requesting user
*PoliciesApi* | [**get_policy**](docs/PoliciesApi.md#get_policy) | **GET** /api/policies/{code} | GetPolicy: Get Policy
*PoliciesApi* | [**get_policy_collection**](docs/PoliciesApi.md#get_policy_collection) | **GET** /api/policycollections/{code} | GetPolicyCollection: Get PolicyCollection
*PoliciesApi* | [**list_policies**](docs/PoliciesApi.md#list_policies) | **GET** /api/policies | ListPolicies: List Policies
*PoliciesApi* | [**list_policy_collections**](docs/PoliciesApi.md#list_policy_collections) | **GET** /api/policycollections | ListPolicyCollections: List PolicyCollections
*PoliciesApi* | [**page_policies**](docs/PoliciesApi.md#page_policies) | **GET** /api/policies/page | PagePolicies: Page Policies
*PoliciesApi* | [**page_policy_collections**](docs/PoliciesApi.md#page_policy_collections) | **GET** /api/policycollections/page | PagePolicyCollections: Page PolicyCollections
*PoliciesApi* | [**remove_from_policy_collection**](docs/PoliciesApi.md#remove_from_policy_collection) | **POST** /api/policycollections/{code}/remove | RemoveFromPolicyCollection: Remove From PolicyCollection
*PoliciesApi* | [**update_policy**](docs/PoliciesApi.md#update_policy) | **PUT** /api/policies/{code} | UpdatePolicy: Update Policy
*PoliciesApi* | [**update_policy_collection**](docs/PoliciesApi.md#update_policy_collection) | **PUT** /api/policycollections/{code} | UpdatePolicyCollection: Update PolicyCollection
*PolicyTemplatesApi* | [**create_policy_template**](docs/PolicyTemplatesApi.md#create_policy_template) | **POST** /api/policytemplates | [EXPERIMENTAL] CreatePolicyTemplate: Create a Policy Template
*PolicyTemplatesApi* | [**delete_policy_template**](docs/PolicyTemplatesApi.md#delete_policy_template) | **DELETE** /api/policytemplates/{code} | [EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template
*PolicyTemplatesApi* | [**generate_policy_from_template**](docs/PolicyTemplatesApi.md#generate_policy_from_template) | **POST** /api/policytemplates/$generatepolicy | [EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template
*PolicyTemplatesApi* | [**get_policy_template**](docs/PolicyTemplatesApi.md#get_policy_template) | **GET** /api/policytemplates/{code} | [EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template
*PolicyTemplatesApi* | [**list_policy_templates**](docs/PolicyTemplatesApi.md#list_policy_templates) | **GET** /api/policytemplates | [EXPERIMENTAL] ListPolicyTemplates: List Policy Templates
*PolicyTemplatesApi* | [**update_policy_template**](docs/PolicyTemplatesApi.md#update_policy_template) | **PUT** /api/policytemplates/{code} | [EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template
*RolesApi* | [**add_policy_collection_to_role**](docs/RolesApi.md#add_policy_collection_to_role) | **POST** /api/roles/{scope}/{code}/policycollections | AddPolicyCollectionToRole: Add policy collections to a role
*RolesApi* | [**create_role**](docs/RolesApi.md#create_role) | **POST** /api/roles | CreateRole: Create Role
*RolesApi* | [**delete_role**](docs/RolesApi.md#delete_role) | **DELETE** /api/roles/{code} | DeleteRole: Delete Role
*RolesApi* | [**get_role**](docs/RolesApi.md#get_role) | **GET** /api/roles/{code} | GetRole: Get Role
*RolesApi* | [**list_roles**](docs/RolesApi.md#list_roles) | **GET** /api/roles | ListRoles: List Roles
*RolesApi* | [**remove_policy_collection_from_role**](docs/RolesApi.md#remove_policy_collection_from_role) | **DELETE** /api/roles/{scope}/{code}/policycollections/{policycollectionscope}/{policycollectioncode} | RemovePolicyCollectionFromRole: Remove policy collection from role
*RolesApi* | [**update_role**](docs/RolesApi.md#update_role) | **PUT** /api/roles/{code} | UpdateRole: Update Role
*UserRolesApi* | [**add_policy_collection_to_user_role**](docs/UserRolesApi.md#add_policy_collection_to_user_role) | **POST** /api/userroles/{userid}/policycollections | AddPolicyCollectionToUserRole: Add a policy collection to a user-role
*UserRolesApi* | [**add_policy_to_user_role**](docs/UserRolesApi.md#add_policy_to_user_role) | **POST** /api/userroles/{userid}/policies | AddPolicyToUserRole: Add a policy to a user-role
*UserRolesApi* | [**create_user_role**](docs/UserRolesApi.md#create_user_role) | **POST** /api/userroles | CreateUserRole: Create a user-role
*UserRolesApi* | [**delete_user_role**](docs/UserRolesApi.md#delete_user_role) | **DELETE** /api/userroles/{userid} | DeleteUserRole: Delete a user-role
*UserRolesApi* | [**get_user_role**](docs/UserRolesApi.md#get_user_role) | **GET** /api/userroles/{userid} | GetUserRole: Get a user-role
*UserRolesApi* | [**list_user_roles**](docs/UserRolesApi.md#list_user_roles) | **GET** /api/userroles | ListUserRoles: List user-roles
*UserRolesApi* | [**remove_policy_collection_from_user_role**](docs/UserRolesApi.md#remove_policy_collection_from_user_role) | **DELETE** /api/userroles/{userid}/policycollections/{policyCollectionScope}/{policyCollectionCode} | RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role
*UserRolesApi* | [**remove_policy_from_user_role**](docs/UserRolesApi.md#remove_policy_from_user_role) | **DELETE** /api/userroles/{userid}/policies/{policyScope}/{policyCode} | RemovePolicyFromUserRole: Remove a policy from a user-role
*UserRolesApi* | [**update_user_role**](docs/UserRolesApi.md#update_user_role) | **POST** /api/userroles/{userid}/update | UpdateUserRole: Update a user-role


<a id="documentation-for-models"></a>
## Documentation for Models

 - [AccessControlledAction](docs/AccessControlledAction.md)
 - [AccessControlledResource](docs/AccessControlledResource.md)
 - [ActionId](docs/ActionId.md)
 - [AddPolicyCollectionToRoleRequest](docs/AddPolicyCollectionToRoleRequest.md)
 - [AddPolicyToRoleRequest](docs/AddPolicyToRoleRequest.md)
 - [AddToPolicyCollectionRequest](docs/AddToPolicyCollectionRequest.md)
 - [AsAtPredicateContract](docs/AsAtPredicateContract.md)
 - [AsAtRangeForSpec](docs/AsAtRangeForSpec.md)
 - [AsAtRelative](docs/AsAtRelative.md)
 - [AttachedPolicyDefinitionResponse](docs/AttachedPolicyDefinitionResponse.md)
 - [DateQuality](docs/DateQuality.md)
 - [DateUnit](docs/DateUnit.md)
 - [EffectiveDateHasQuality](docs/EffectiveDateHasQuality.md)
 - [EffectiveDateRelative](docs/EffectiveDateRelative.md)
 - [EffectiveRange](docs/EffectiveRange.md)
 - [EntitlementMetadata](docs/EntitlementMetadata.md)
 - [EvaluationRequest](docs/EvaluationRequest.md)
 - [EvaluationResponse](docs/EvaluationResponse.md)
 - [EvaluationResult](docs/EvaluationResult.md)
 - [ForSpec](docs/ForSpec.md)
 - [GeneratePolicyFromTemplateRequest](docs/GeneratePolicyFromTemplateRequest.md)
 - [GeneratedPolicyComponents](docs/GeneratedPolicyComponents.md)
 - [Grant](docs/Grant.md)
 - [HowSpec](docs/HowSpec.md)
 - [IdSelectorDefinition](docs/IdSelectorDefinition.md)
 - [IdentifierPartSchema](docs/IdentifierPartSchema.md)
 - [IfExpression](docs/IfExpression.md)
 - [IfFeatureChainExpression](docs/IfFeatureChainExpression.md)
 - [IfIdentityClaimExpression](docs/IfIdentityClaimExpression.md)
 - [IfIdentityScopeExpression](docs/IfIdentityScopeExpression.md)
 - [IfRequestHeaderExpression](docs/IfRequestHeaderExpression.md)
 - [KeyValuePairOfStringToString](docs/KeyValuePairOfStringToString.md)
 - [Link](docs/Link.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [LusidValidationProblemDetails](docs/LusidValidationProblemDetails.md)
 - [MatchAllSelectorDefinition](docs/MatchAllSelectorDefinition.md)
 - [MetadataExpression](docs/MetadataExpression.md)
 - [MetadataSelectorDefinition](docs/MetadataSelectorDefinition.md)
 - [NonTransitiveSupervisorRoleResource](docs/NonTransitiveSupervisorRoleResource.md)
 - [Operator](docs/Operator.md)
 - [PointInTimeSpecification](docs/PointInTimeSpecification.md)
 - [PolicyCollectionCreationRequest](docs/PolicyCollectionCreationRequest.md)
 - [PolicyCollectionId](docs/PolicyCollectionId.md)
 - [PolicyCollectionResponse](docs/PolicyCollectionResponse.md)
 - [PolicyCollectionUpdateRequest](docs/PolicyCollectionUpdateRequest.md)
 - [PolicyCreationRequest](docs/PolicyCreationRequest.md)
 - [PolicyId](docs/PolicyId.md)
 - [PolicyIdRoleResource](docs/PolicyIdRoleResource.md)
 - [PolicyResponse](docs/PolicyResponse.md)
 - [PolicySelectorDefinition](docs/PolicySelectorDefinition.md)
 - [PolicyTemplateCreationRequest](docs/PolicyTemplateCreationRequest.md)
 - [PolicyTemplateResponse](docs/PolicyTemplateResponse.md)
 - [PolicyTemplateUpdateRequest](docs/PolicyTemplateUpdateRequest.md)
 - [PolicyTemplatedSelector](docs/PolicyTemplatedSelector.md)
 - [PolicyType](docs/PolicyType.md)
 - [PolicyUpdateRequest](docs/PolicyUpdateRequest.md)
 - [RelativeToDateTime](docs/RelativeToDateTime.md)
 - [RemoveFromPolicyCollectionRequest](docs/RemoveFromPolicyCollectionRequest.md)
 - [RequestDetails](docs/RequestDetails.md)
 - [RequestedActionKey](docs/RequestedActionKey.md)
 - [ResourceDetails](docs/ResourceDetails.md)
 - [ResourceListOfAccessControlledResource](docs/ResourceListOfAccessControlledResource.md)
 - [ResourceListOfPolicyCollectionResponse](docs/ResourceListOfPolicyCollectionResponse.md)
 - [ResourceListOfPolicyResponse](docs/ResourceListOfPolicyResponse.md)
 - [ResourceListOfPolicyTemplateResponse](docs/ResourceListOfPolicyTemplateResponse.md)
 - [ResourceListOfUserRoleResponse](docs/ResourceListOfUserRoleResponse.md)
 - [RoleCreationRequest](docs/RoleCreationRequest.md)
 - [RoleId](docs/RoleId.md)
 - [RoleResourceRequest](docs/RoleResourceRequest.md)
 - [RoleResponse](docs/RoleResponse.md)
 - [RoleUpdateRequest](docs/RoleUpdateRequest.md)
 - [SelectorDefinition](docs/SelectorDefinition.md)
 - [TemplateMetadata](docs/TemplateMetadata.md)
 - [TemplateSelection](docs/TemplateSelection.md)
 - [TextOperator](docs/TextOperator.md)
 - [UserRoleCreationRequest](docs/UserRoleCreationRequest.md)
 - [UserRoleResponse](docs/UserRoleResponse.md)
 - [UserRoleUpdateRequest](docs/UserRoleUpdateRequest.md)
 - [WhenSpec](docs/WhenSpec.md)

