class PollController < ApplicationController
  before_action :set_poll, only: [:show, :edit, :update, :destroy]

  # GET /poll
  def index
    @polls = Poll.all
    render json: @polls
  end

  # GET /poll/1
  def show
    render json: @poll
  end

  # POST /poll
  def create
    @poll = Poll.new(poll_params)

    if @poll.save
      render json: @poll, status: :created
    else
      render json: @poll.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /poll/1
  def update
    if @poll.update(poll_params)
      render json: @poll
    else
      render json: @poll.errors, status: :unprocessable_entity
    end
  end

  # DELETE /poll/1
  def destroy
    @poll.destroy
    head :no_content
  end

  private

  def set_poll
    @poll = Poll.find(params[:id])
  end

  def poll_params
    params.require(:poll).permit(:name)
  end
end
