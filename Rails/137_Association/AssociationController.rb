class AssociationController < ApplicationController
  before_action :set_association, only: [:show, :edit, :update, :destroy]

  # GET /association
  def index
    @associations = Association.all
    render json: @associations
  end

  # GET /association/1
  def show
    render json: @association
  end

  # POST /association
  def create
    @association = Association.new(association_params)

    if @association.save
      render json: @association, status: :created
    else
      render json: @association.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /association/1
  def update
    if @association.update(association_params)
      render json: @association
    else
      render json: @association.errors, status: :unprocessable_entity
    end
  end

  # DELETE /association/1
  def destroy
    @association.destroy
    head :no_content
  end

  private

  def set_association
    @association = Association.find(params[:id])
  end

  def association_params
    params.require(:association).permit(:name)
  end
end
