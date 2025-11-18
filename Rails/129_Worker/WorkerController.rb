class WorkerController < ApplicationController
  before_action :set_worker, only: [:show, :edit, :update, :destroy]

  # GET /worker
  def index
    @workers = Worker.all
    render json: @workers
  end

  # GET /worker/1
  def show
    render json: @worker
  end

  # POST /worker
  def create
    @worker = Worker.new(worker_params)

    if @worker.save
      render json: @worker, status: :created
    else
      render json: @worker.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /worker/1
  def update
    if @worker.update(worker_params)
      render json: @worker
    else
      render json: @worker.errors, status: :unprocessable_entity
    end
  end

  # DELETE /worker/1
  def destroy
    @worker.destroy
    head :no_content
  end

  private

  def set_worker
    @worker = Worker.find(params[:id])
  end

  def worker_params
    params.require(:worker).permit(:name)
  end
end
