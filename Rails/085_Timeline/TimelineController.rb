class TimelineController < ApplicationController
  before_action :set_timeline, only: [:show, :edit, :update, :destroy]

  # GET /timeline
  def index
    @timelines = Timeline.all
    render json: @timelines
  end

  # GET /timeline/1
  def show
    render json: @timeline
  end

  # POST /timeline
  def create
    @timeline = Timeline.new(timeline_params)

    if @timeline.save
      render json: @timeline, status: :created
    else
      render json: @timeline.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /timeline/1
  def update
    if @timeline.update(timeline_params)
      render json: @timeline
    else
      render json: @timeline.errors, status: :unprocessable_entity
    end
  end

  # DELETE /timeline/1
  def destroy
    @timeline.destroy
    head :no_content
  end

  private

  def set_timeline
    @timeline = Timeline.find(params[:id])
  end

  def timeline_params
    params.require(:timeline).permit(:name)
  end
end
