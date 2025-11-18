class QueueController < ApplicationController
  before_action :set_queue, only: [:show, :edit, :update, :destroy]

  # GET /queue
  def index
    @queues = Queue.all
    render json: @queues
  end

  # GET /queue/1
  def show
    render json: @queue
  end

  # POST /queue
  def create
    @queue = Queue.new(queue_params)

    if @queue.save
      render json: @queue, status: :created
    else
      render json: @queue.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /queue/1
  def update
    if @queue.update(queue_params)
      render json: @queue
    else
      render json: @queue.errors, status: :unprocessable_entity
    end
  end

  # DELETE /queue/1
  def destroy
    @queue.destroy
    head :no_content
  end

  private

  def set_queue
    @queue = Queue.find(params[:id])
  end

  def queue_params
    params.require(:queue).permit(:name)
  end
end
