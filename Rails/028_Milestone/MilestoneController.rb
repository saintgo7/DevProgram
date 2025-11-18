class MilestoneController < ApplicationController
  before_action :set_milestone, only: [:show, :edit, :update, :destroy]

  # GET /milestone
  def index
    @milestones = Milestone.all
    render json: @milestones
  end

  # GET /milestone/1
  def show
    render json: @milestone
  end

  # POST /milestone
  def create
    @milestone = Milestone.new(milestone_params)

    if @milestone.save
      render json: @milestone, status: :created
    else
      render json: @milestone.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /milestone/1
  def update
    if @milestone.update(milestone_params)
      render json: @milestone
    else
      render json: @milestone.errors, status: :unprocessable_entity
    end
  end

  # DELETE /milestone/1
  def destroy
    @milestone.destroy
    head :no_content
  end

  private

  def set_milestone
    @milestone = Milestone.find(params[:id])
  end

  def milestone_params
    params.require(:milestone).permit(:name)
  end
end
