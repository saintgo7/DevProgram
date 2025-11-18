class SyncController < ApplicationController
  before_action :set_sync, only: [:show, :edit, :update, :destroy]

  # GET /sync
  def index
    @syncs = Sync.all
    render json: @syncs
  end

  # GET /sync/1
  def show
    render json: @sync
  end

  # POST /sync
  def create
    @sync = Sync.new(sync_params)

    if @sync.save
      render json: @sync, status: :created
    else
      render json: @sync.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sync/1
  def update
    if @sync.update(sync_params)
      render json: @sync
    else
      render json: @sync.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sync/1
  def destroy
    @sync.destroy
    head :no_content
  end

  private

  def set_sync
    @sync = Sync.find(params[:id])
  end

  def sync_params
    params.require(:sync).permit(:name)
  end
end
