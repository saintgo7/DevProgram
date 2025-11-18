class SchedulerController < ApplicationController
  before_action :set_scheduler, only: [:show, :edit, :update, :destroy]

  # GET /scheduler
  def index
    @schedulers = Scheduler.all
    render json: @schedulers
  end

  # GET /scheduler/1
  def show
    render json: @scheduler
  end

  # POST /scheduler
  def create
    @scheduler = Scheduler.new(scheduler_params)

    if @scheduler.save
      render json: @scheduler, status: :created
    else
      render json: @scheduler.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /scheduler/1
  def update
    if @scheduler.update(scheduler_params)
      render json: @scheduler
    else
      render json: @scheduler.errors, status: :unprocessable_entity
    end
  end

  # DELETE /scheduler/1
  def destroy
    @scheduler.destroy
    head :no_content
  end

  private

  def set_scheduler
    @scheduler = Scheduler.find(params[:id])
  end

  def scheduler_params
    params.require(:scheduler).permit(:name)
  end
end
