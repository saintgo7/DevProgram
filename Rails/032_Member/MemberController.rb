class MemberController < ApplicationController
  before_action :set_member, only: [:show, :edit, :update, :destroy]

  # GET /member
  def index
    @members = Member.all
    render json: @members
  end

  # GET /member/1
  def show
    render json: @member
  end

  # POST /member
  def create
    @member = Member.new(member_params)

    if @member.save
      render json: @member, status: :created
    else
      render json: @member.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /member/1
  def update
    if @member.update(member_params)
      render json: @member
    else
      render json: @member.errors, status: :unprocessable_entity
    end
  end

  # DELETE /member/1
  def destroy
    @member.destroy
    head :no_content
  end

  private

  def set_member
    @member = Member.find(params[:id])
  end

  def member_params
    params.require(:member).permit(:name)
  end
end
