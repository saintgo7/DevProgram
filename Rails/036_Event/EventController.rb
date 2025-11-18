class EventController < ApplicationController
  before_action :set_event, only: [:show, :edit, :update, :destroy]

  # GET /event
  def index
    @events = Event.all
    render json: @events
  end

  # GET /event/1
  def show
    render json: @event
  end

  # POST /event
  def create
    @event = Event.new(event_params)

    if @event.save
      render json: @event, status: :created
    else
      render json: @event.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /event/1
  def update
    if @event.update(event_params)
      render json: @event
    else
      render json: @event.errors, status: :unprocessable_entity
    end
  end

  # DELETE /event/1
  def destroy
    @event.destroy
    head :no_content
  end

  private

  def set_event
    @event = Event.find(params[:id])
  end

  def event_params
    params.require(:event).permit(:name)
  end
end
