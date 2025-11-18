class ScheduleController < ApplicationController
  before_action :set_schedule, only: [:show, :edit, :update, :destroy]

  # GET /schedule
  def index
    @schedules = Schedule.all
    render json: @schedules
  end

  # GET /schedule/1
  def show
    render json: @schedule
  end

  # POST /schedule
  def create
    @schedule = Schedule.new(schedule_params)

    if @schedule.save
      render json: @schedule, status: :created
    else
      render json: @schedule.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /schedule/1
  def update
    if @schedule.update(schedule_params)
      render json: @schedule
    else
      render json: @schedule.errors, status: :unprocessable_entity
    end
  end

  # DELETE /schedule/1
  def destroy
    @schedule.destroy
    head :no_content
  end

  private

  def set_schedule
    @schedule = Schedule.find(params[:id])
  end

  def schedule_params
    params.require(:schedule).permit(:name)
  end
end
