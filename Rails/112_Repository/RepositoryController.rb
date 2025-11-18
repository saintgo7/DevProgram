class RepositoryController < ApplicationController
  before_action :set_repository, only: [:show, :edit, :update, :destroy]

  # GET /repository
  def index
    @repositorys = Repository.all
    render json: @repositorys
  end

  # GET /repository/1
  def show
    render json: @repository
  end

  # POST /repository
  def create
    @repository = Repository.new(repository_params)

    if @repository.save
      render json: @repository, status: :created
    else
      render json: @repository.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /repository/1
  def update
    if @repository.update(repository_params)
      render json: @repository
    else
      render json: @repository.errors, status: :unprocessable_entity
    end
  end

  # DELETE /repository/1
  def destroy
    @repository.destroy
    head :no_content
  end

  private

  def set_repository
    @repository = Repository.find(params[:id])
  end

  def repository_params
    params.require(:repository).permit(:name)
  end
end
