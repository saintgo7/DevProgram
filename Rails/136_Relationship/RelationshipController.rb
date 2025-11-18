class RelationshipController < ApplicationController
  before_action :set_relationship, only: [:show, :edit, :update, :destroy]

  # GET /relationship
  def index
    @relationships = Relationship.all
    render json: @relationships
  end

  # GET /relationship/1
  def show
    render json: @relationship
  end

  # POST /relationship
  def create
    @relationship = Relationship.new(relationship_params)

    if @relationship.save
      render json: @relationship, status: :created
    else
      render json: @relationship.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /relationship/1
  def update
    if @relationship.update(relationship_params)
      render json: @relationship
    else
      render json: @relationship.errors, status: :unprocessable_entity
    end
  end

  # DELETE /relationship/1
  def destroy
    @relationship.destroy
    head :no_content
  end

  private

  def set_relationship
    @relationship = Relationship.find(params[:id])
  end

  def relationship_params
    params.require(:relationship).permit(:name)
  end
end
