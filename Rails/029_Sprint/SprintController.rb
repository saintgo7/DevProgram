class SprintController < ApplicationController
  before_action :set_sprint, only: [:show, :edit, :update, :destroy]

  # GET /sprint
  def index
    @sprints = Sprint.all
    render json: @sprints
  end

  # GET /sprint/1
  def show
    render json: @sprint
  end

  # POST /sprint
  def create
    @sprint = Sprint.new(sprint_params)

    if @sprint.save
      render json: @sprint, status: :created
    else
      render json: @sprint.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sprint/1
  def update
    if @sprint.update(sprint_params)
      render json: @sprint
    else
      render json: @sprint.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sprint/1
  def destroy
    @sprint.destroy
    head :no_content
  end

  private

  def set_sprint
    @sprint = Sprint.find(params[:id])
  end

  def sprint_params
    params.require(:sprint).permit(:name)
  end
end
