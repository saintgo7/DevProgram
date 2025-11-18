class PlanController < ApplicationController
  before_action :set_plan, only: [:show, :edit, :update, :destroy]

  # GET /plan
  def index
    @plans = Plan.all
    render json: @plans
  end

  # GET /plan/1
  def show
    render json: @plan
  end

  # POST /plan
  def create
    @plan = Plan.new(plan_params)

    if @plan.save
      render json: @plan, status: :created
    else
      render json: @plan.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /plan/1
  def update
    if @plan.update(plan_params)
      render json: @plan
    else
      render json: @plan.errors, status: :unprocessable_entity
    end
  end

  # DELETE /plan/1
  def destroy
    @plan.destroy
    head :no_content
  end

  private

  def set_plan
    @plan = Plan.find(params[:id])
  end

  def plan_params
    params.require(:plan).permit(:name)
  end
end
