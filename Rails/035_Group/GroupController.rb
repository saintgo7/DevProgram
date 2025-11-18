class GroupController < ApplicationController
  before_action :set_group, only: [:show, :edit, :update, :destroy]

  # GET /group
  def index
    @groups = Group.all
    render json: @groups
  end

  # GET /group/1
  def show
    render json: @group
  end

  # POST /group
  def create
    @group = Group.new(group_params)

    if @group.save
      render json: @group, status: :created
    else
      render json: @group.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /group/1
  def update
    if @group.update(group_params)
      render json: @group
    else
      render json: @group.errors, status: :unprocessable_entity
    end
  end

  # DELETE /group/1
  def destroy
    @group.destroy
    head :no_content
  end

  private

  def set_group
    @group = Group.find(params[:id])
  end

  def group_params
    params.require(:group).permit(:name)
  end
end
