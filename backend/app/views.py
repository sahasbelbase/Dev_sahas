# app/views.py

# Import existing models and serializers
from app.models import Hotel, AddressType, Person, Branch
from app.serializers import HotelSchema, AddressTypeSchema, PersonSchema, BranchSchema

branch_schema = BranchSchema()
branches_schema = BranchSchema(many=True)

# API route to get all branches with hotel and address type details
@app.route('/api/branches', methods=['GET'])
def get_all_branches():
    branches = Branch.query.all()
    result = branches_schema.dump(branches)

    # Enhance the result with additional details (e.g., hotel and address type names)
    enhanced_result = []
    for branch_data in result:
        hotel = Hotel.query.get(branch_data['hotel_id'])
        address_type = AddressType.query.get(branch_data['address_type_id'])

        enhanced_branch_data = {
            **branch_data,
            'hotel_name': hotel.name if hotel else None,
            'address_type': address_type.type if address_type else None
        }

        enhanced_result.append(enhanced_branch_data)

    return jsonify(enhanced_result)

# API route to create a branch
@app.route('/api/branches', methods=['POST'])
def create_branch():
    data = request.get_json()

    # Validate Input Data
    if 'hotel_id' not in data or 'address_type_id' not in data or 'branch_name' not in data:
        return jsonify(message='Invalid data. Missing required fields.'), 400

    # Create Branch
    new_branch = Branch(
        hotel_id=data['hotel_id'],
        address_type_id=data['address_type_id'],
        branch_name=data['branch_name'],
        country=data.get('country'),
        city=data.get('city'),
        street_name=data.get('street_name'),
        user_person_id=data.get('user_person_id')
    )
    db.session.add(new_branch)
    db.session.commit()

    # Serialize the branch
    result = branch_schema.dump(new_branch)

    return jsonify(message='Branch created successfully', branch=result), 201

# API route to update a branch
@app.route('/api/branches/<int:branch_id>', methods=['PUT'])
def update_branch(branch_id):
    branch = Branch.query.get(branch_id)

    if not branch:
        return jsonify(message=f'Branch with ID {branch_id} not found.'), 404

    data = request.get_json()

    # Update branch fields
    branch.hotel_id = data.get('hotel_id', branch.hotel_id)
    branch.address_type_id = data.get('address_type_id', branch.address_type_id)
    branch.branch_name = data.get('branch_name', branch.branch_name)
    branch.country = data.get('country', branch.country)
    branch.city = data.get('city', branch.city)
    branch.street_name = data.get('street_name', branch.street_name)
    branch.user_person_id = data.get('user_person_id', branch.user_person_id)

    db.session.commit()

    result = branch_schema.dump(branch)
    return jsonify(message='Branch updated successfully', branch=result)

# API route to delete a branch
@app.route('/api/branches/<int:branch_id>', methods=['DELETE'])
def delete_branch(branch_id):
    branch = Branch.query.get(branch_id)

    if not branch:
        return jsonify(message=f'Branch with ID {branch_id} not found.'), 404

    db.session.delete(branch)
    db.session.commit()

    return jsonify(message='Branch deleted successfully'), 200
