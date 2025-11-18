class JobController < ApplicationController
  before_action :set_job, only: [:show, :edit, :update, :destroy]

  # GET /job
  def index
    @jobs = Job.all
    render json: @jobs
  end

  # GET /job/1
  def show
    render json: @job
  end

  # POST /job
  def create
    @job = Job.new(job_params)

    if @job.save
      render json: @job, status: :created
    else
      render json: @job.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /job/1
  def update
    if @job.update(job_params)
      render json: @job
    else
      render json: @job.errors, status: :unprocessable_entity
    end
  end

  # DELETE /job/1
  def destroy
    @job.destroy
    head :no_content
  end

  private

  def set_job
    @job = Job.find(params[:id])
  end

  def job_params
    params.require(:job).permit(:name)
  end
end
