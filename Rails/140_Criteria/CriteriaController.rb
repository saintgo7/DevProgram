class CriteriaController < ApplicationController
  before_action :set_criteria, only: [:show, :edit, :update, :destroy]

  # GET /criteria
  def index
    @criterias = Criteria.all
    render json: @criterias
  end

  # GET /criteria/1
  def show
    render json: @criteria
  end

  # POST /criteria
  def create
    @criteria = Criteria.new(criteria_params)

    if @criteria.save
      render json: @criteria, status: :created
    else
      render json: @criteria.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /criteria/1
  def update
    if @criteria.update(criteria_params)
      render json: @criteria
    else
      render json: @criteria.errors, status: :unprocessable_entity
    end
  end

  # DELETE /criteria/1
  def destroy
    @criteria.destroy
    head :no_content
  end

  private

  def set_criteria
    @criteria = Criteria.find(params[:id])
  end

  def criteria_params
    params.require(:criteria).permit(:name)
  end
end
