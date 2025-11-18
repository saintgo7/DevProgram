class CalendarController < ApplicationController
  before_action :set_calendar, only: [:show, :edit, :update, :destroy]

  # GET /calendar
  def index
    @calendars = Calendar.all
    render json: @calendars
  end

  # GET /calendar/1
  def show
    render json: @calendar
  end

  # POST /calendar
  def create
    @calendar = Calendar.new(calendar_params)

    if @calendar.save
      render json: @calendar, status: :created
    else
      render json: @calendar.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /calendar/1
  def update
    if @calendar.update(calendar_params)
      render json: @calendar
    else
      render json: @calendar.errors, status: :unprocessable_entity
    end
  end

  # DELETE /calendar/1
  def destroy
    @calendar.destroy
    head :no_content
  end

  private

  def set_calendar
    @calendar = Calendar.find(params[:id])
  end

  def calendar_params
    params.require(:calendar).permit(:name)
  end
end
